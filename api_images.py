import requests

response = requests.get("https://www.flickr.com/photos/sneequaye/29938528706/in/photolist-MByMxq-pPMXJr-q7hVBw-q79S2K-Uqevqi-DHjPqm-zyVLqX-pPKNN5-pamgzo-q5vkxE-pao7zV-pammtb-q6YBHa-pPLHT2-pPNXTq-papGvt-pak6q7-q6ZpGV-paoa4x-q7ftGu-paoTaB-zhjXd7-q78wpa-2hFfBPN-2heu5Kd-q54njs-q6XKSt-pamE7Y-pPLdw7-panWCk-pPHZ14-q7qTcz-pPPjUy-q6YzdR-pPMK4r-q7fr2Q-pPKyfB-paqoGv-papK4V-pPLp5S-q53cEj-tNhZAP-g3t7YB-g3sqw5-47v2u-3LG5KA-g3sGzC-g3shdc-2hBrFFu-CNRV5v")

print(response.status_code)