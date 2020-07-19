#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import dateparser
from operator import itemgetter
import re


class AwsShdRss():
    def __init__(self, desc=False):
        self.desc = desc
        self.url = 'https://status.aws.amazon.com/rss/all.rss'
        self.entries = self.get_entries()

    def get_entries(self):
        """get_entries

        Get RSS entry

        Raises:
            e: Exception

        Returns:
            [dict]: rss.entries
        """
        try:
            feed = feedparser.parse(self.url)
        except Exception as e:
            raise e

        entries = []
        for entry in feed['entries']:
            epoch = dateparser.parse(entry['published']).timestamp()
            row = {
                'epoch': int(epoch),
                'id': entry['id'],
                'published': entry['published'],
                'summary': entry['summary'],
                'title': entry['title'],
            }

            # e.g.) id: http://status.aws.amazon.com/#{service}-{region}_{epoch}
            guid = entry['id'].split('#')[1]
            guid_service = guid.split('_')[0]
            if guid_service.count('-') > 2:
                # regional
                regex = r'^(.[^-]*)'
                match_obj = re.search(regex, guid_service)
                row['service'] = match_obj.group()
                row['region'] = guid_service.replace(
                    f"{row['service']}-", "")
            else:
                # global
                row['service'] = guid_service
                row['region'] = 'global'

            entries.append(row)

        result = sorted(entries, key=itemgetter('epoch'), reverse=self.desc)
        return result

    def get_updates(self, since_dt, until_dt, include_global=True, include_regions=[]):
        """get_updates

        Args:
            since_dt ([type]): The start of the time range
            until_dt ([type]): The end of the time range
            include_global (bool, optional): Include global service updates. Defaults to True.
            include_regions (list, optional): Include specific regional service updates. Defaults to [], includes all regions.

        Returns:
            [dict]: rss.entries
        """
        since = since_dt.timestamp()
        until = until_dt.timestamp()

        entries = []
        for entry in self.entries:
            if since <= entry['epoch'] and entry['epoch'] < until:
                if entry['region'] == 'global' and include_global:
                    entries.append(entry)
                else:
                    if len(include_regions) == 0 or entry['region'] in include_regions:
                        entries.append(entry)

        return entries
