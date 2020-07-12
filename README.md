# hiag
Test Project for open Hab integration at hiag

Setup:

1. Burn Openhabian Image with standart openhabian.conf file
2. Install standart setup
3.Connect by SSH to controller and open config: sudo openhabian-config
* Change Username and Passwort in menu
* Move root to USB
* Install Grafana and Influxdb addon

3. Configuration with paper UI
* Install exec binding
* Use regex transformation
* Install shelly binding
* Install mqtt broker moquette
* Configure influxdb persistance

4. Install Modules:
* sudo -u openhab pip3 install --target=/etc/openhab2/scripts/ pandas
* sudo apt get install libatlas-base-dev

5. Start application Setup
* Add Scripts to etc/openhab2/scripts/
* Add influx.persist to etc/openhab2/persistence/
* Add exec.whitelist to etc/openhab2/misc/
Exec Binding:
/usr/bin/python3@@/etc/openhab2/scripts/API.py@@%2$s
