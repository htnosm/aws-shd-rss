# aws-shd-rss
Check AWS Service Health Dashboard RSS

## Requirements

* dateparser
* feedparser

## Installation

### From pip

```
pip install git+https://github.com/htnosm/aws-shd-rss.git
```

### From source

```
python setup.py install
```

## Usage

```
from aws_shd_rss import AwsShdRss
from datetime import datetime, timedelta

rss = AwsShdRss()

until_dt = datetime.now()
since_dt = until_dt - timedelta(minutes=5)

entries = rss.get_updates(since_dt, until_dt, include_global=True, include_regions=include_regions)

# specific region
include_regions = [
    "ap-northeast-1",
    "us-east-1",
]

entries = rss.get_updates(since_dt, until_dt, include_global=False, include_regions=include_regions)
```
