# fetch-oid-description
This repository contains a web scraper that can help you match OIDs with their descriptions 

On other days, I worked with the SNMP protocol, which stands for Simple Network Management Protocol. I wanted to create a dashboard for network monitoring, and the workflow can be summarized like this: the snmp_exporter collects the desired metrics from a Cisco ASA device, sends them to Prometheus, and then visualizes them in Grafana.  


#### Cisco ASA -----> snmp_exporter -----> Prometheus -----> Grafana -----> Happy Me :)  

In my experience, SNMP isn’t as "Simple" as its name implies. I found the naming conventions for metrics to be quite complex, especially since they include IP addresses and interfaces from which the metrics are collected.  

Additionally, I faced a significant challenge: I couldn’t find a single resource that lists all the metrics with descriptions and provides a convenient way to search through them. When creating a dashboard, I usually rely on some key terms that should be reflected in the description or name of the metric. Unfortunately, no resource offers this type of search functionality. Users are left either blindly clicking through every possible OID or needing to know the exact metric beforehand.

## Main point
To address this problem and make my life easier, I wrote a web scraper that takes a file containing OIDs as input and generates a text document with detailed information about each specific OID. It does this using the `requests` and `BeautifulSoup` libraries, scraping the necessary data from the website `oid-base.com` by extracting information from relevant tags. While it’s far from perfect and may stop working if the website updates, for now, it serves its purpose.

Other resources that helped me understand SNMP:
- Hvala and many thanks to @haad https://github.com/haad for https://gist.github.com/haad/4237509
- https://www.cisco.com/c/en/us/td/docs/security/asa/asa84/configuration/guide/asa_84_cli_config/monitor_snmp.html#70428
- https://snmp.cloudapps.cisco.com/Support/SNMP/do/BrowseOID.do?local=en  -- you need to login
- https://www.rfc-editor.org/rfc/rfc1157
- https://github.com/prometheus/snmp_exporter
- https://oid-base.com/faq.htm#leaf

Please, feel free to reach me out in [Discussions](https://github.com/elshirak/fetch-oid-description/discussions) or [Issues](https://github.com/elshirak/fetch-oid-description/issues) sections. Also, write me a line if you know any other way to work with OIDs
