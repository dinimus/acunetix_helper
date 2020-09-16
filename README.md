# acunetix_helper
Scripts for auto-creating and running scans, reports downloading
Change an API key and a server address before running the scripts.

## Auto-creating and running scans
Feed the script a .txt file with a list of URLs of the sites to scan:
```
kali@kali:/$ python creator.py urls.txt test_company
1. Created https://test1.org
2. Created http://test2.com
```

## Auto-downloading scan reports
Feed the script a .txt file with a list of URLs of the sites to download reports:
```
kali@kali:/$ python downloader.py urls.txt 2020-09-01
1. Report created: 20200910_Developer_https_test1_org.html
2. Report created: 20200910_Developer_http_test2_com.html
```
