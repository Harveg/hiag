# hiag
Test Project for open Hab integration at hiag

Setup:

1. Burn Openhabian Image with standart openhabian.conf file
2. Install standart setup
3. Connect by SSH to controller and open config: sudo openhabian-config
* Change Username and Passwort in menu
* Move root to USB
* Install Grafana and Influxdb addon
* Install Node-Red addon

4. Backup existing openhab configuration if exist (optionaly)
5. Configuration with paper UI
* Install exec binding
* Use regex transformation
* Install shelly binding
* Install mqtt broker moquette
* System Configuration: Configure influxdb persistance
* System Configuration: Configurate IP-Adress and deactivate IPv6

6. Install Modules:
* sudo -u openhab pip3 install --target=/etc/openhab2/scripts/ pandas
* sudo apt get install libatlas-base-dev

7. Start application Setup
* Add Scripts to /etc/openhab2/scripts/
* Add wiki template influxdb.persist to /etc/openhab2/persistence/
* Add exec.whitelist to /etc/openhab2/misc/
* Change influxdb.conf in /etc/influxdb/ ``bind-address = "0.0.0.0:8086"``

### Optional: Exec Binding:
/usr/bin/python3@@/etc/openhab2/scripts/API.py@@%2$s
