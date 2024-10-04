# Running Prometheus
This branch will work with feat--reviews-metrics-tracking branch to run prometheus on your microservice (run them locally for now).

https://prometheus.io/docs/prometheus/latest/getting_started/

1. Download Prometheus
Go to the Prometheus download page and find the correct version for your system. If you're on macOS, choose the darwin build.

2. Extract the Archive
Extract the downloaded archive: `tar -xvzf prometheus-2.53.2.darwin-amd64.tar.gz`.
This will create a folder prometheus-2.53.2.darwin-amd64.

3. Setup Configuration (prometheus.yml)
Ensure that you have a prometheus.yml configuration file in the same folder. Refer to yaml file in this branch

4. Run Prometheus
Navigate to the extracted directory:
`cd prometheus-2.53.2.darwin-amd64`

Then, use the following command to run Prometheus with the provided arguments:
`./prometheus --config.file=prometheus.yml --web.enable-lifecycle --log.level=debug | tee prometheus.log`

This will:
- Start Prometheus with the specified configuration file (prometheus.yml).
- Enable the web lifecycle API (--web.enable-lifecycle), allowing you to reload configurations without restarting Prometheus.
- Set the logging level to debug (--log.level=debug), providing verbose logs.
- Pipe the logs to a file (prometheus.log) while also displaying them in the terminal.

5. Access the Prometheus UI
Once Prometheus is running, you can access the UI by opening your browser and navigating to:
`http://localhost:9090`

6. Verify Targets
To ensure Prometheus is scraping the correct endpoints, go to http://localhost:9090/targets. You should see the Prometheus and Django targets with a green status if they are running and being scraped successfully.


