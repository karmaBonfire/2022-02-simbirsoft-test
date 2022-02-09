%cd%
java -Dwebdriver.firefox.driver=%cd%/geckodriver.exe -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig nodes.json
pause