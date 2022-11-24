# Module 9 Documentation

## Set up Stackdriver monitoring and perform a simple load test using ApacheBench or a similar tool.


1. Create VM Instance in Compute Engine
2. Follow the commands in the SSH of the instance

Sudo apt update
sudo apt install golang-go

3. Type the commands below.

vi hello.go

4. PASTE THE BELOW

package main

import (
    "log"
    "net/http"
)

func helloGoHandler(w http.ResponseWriter, r *http.Request){
    w.Write([]byte("hello net/http\n"))
}
func main(){
    http.HandleFunc("/",helloGoHandler)
    log.Fatal(http.ListenAndServe(":8000",nil))

}


5. In vi mode, i is insert, esc is back. SHIFT+zz saves and quits

6. INSTALL THE MONITORING AGENT

curl -sSO https://dl.google.com/cloudagents/add-monitoring-agent-repo.sh
sudo bash add-monitoring-agent-repo.sh --also-install

7. INSTALL APACHE WORK BENCH

sudo apt-get update
sudo apt-get -y install apache2-utils

8. 

go run hello.go

grab the IP (internal)

curl http://10.128.0.11:8000/
--> should see hello net/http

9. Naviguate to monitoring - dashboard
10. create new dasboard.. create some random tables

11. Type the following commands to load test

ab -n 1000 -c 100 http://10.128.0.11:8001/
