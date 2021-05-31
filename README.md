# UOCIS322 - Project 6 #
Author: Kaetlyn Gibson

Contact Address: kaetlyng@uoregon.edu

## Overview
Brevet time calculator with AJAX, MongoDB, and a RESTful API!

### Background
What are brevets? Brevets are timed rides with controls. Controls are points where a rider must obtain proof of passage, and controle times are the minimum and maximum times by which the rider must arrive at the location.

### The Algorithm
To calculate the opening time, we divide the distance of the control point(in km) by the maximum speed(in km/hr) designated by the location of the control. To calculate the closing time, we divide the distance of the control point(in km) by the minimum speed(in km/hr) designated by the location of the control. Of course, it is slightly more complicated than this, so I recommend taking a look at the examples from here: https://rusa.org/pages/acp-brevet-control-times-calculator.

### Time Calculation
Dividing the distance in kilometers by speed of kilometers per hour results in a time
in hours. To convert into hours and minutes, subtract the whole number of hours and multiply the resulting fractional part by 60. Times are rounded to the nearest minute.

### Tasks

- Created three basic APIs:
  - "http://<host:port>/listAll" should return all open and close times in the database
  - "http://<host:port>/listOpenOnly" should return open times only
  - "http://<host:port>/listCloseOnly" should return close times only
- Two different representations: one in csv, one in JSON. JSON is the default representation for all three.
  - "http://<host:port>/listAll/csv" should return all open and close times in CSV format
  - "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
  - "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

  - "http://<host:port>/listAll/json" should return all open and close times in JSON format
  - "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
  - "http://<host:port>/listCloseOnly/json" should return close times only in JSON format
- Added a query parameter to get top "k" open and close times (examples below)
  - "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format
  - "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
  - "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
  - "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format
- Designed consumer programs to use the service exposed using PHP

## Usage
- Build/run using docker-compose: 
  ```
  docker-compose up -d --build

  ```
- To use the brevet calculator:
  - Launch `http://5555:5000` using web browser
  - Choose a brevet distance
  - Choose begin date and time
  - Enter controle locations in km or miles
  - Submit, to submit values (message will appear if successful)
  - Display, to display values on another page
- To view the APIs via website:
  - Launch `http://5557:5000` using web browser
  - Select desired from the following:
    - From APIs:
      - listAll
      - listOpenOnly
      - listCloseOnly
    - From result representation:
      - Table (extra)
      - CSV
      - JSON (default)
    - View top k results, or not
  - Submit choices using `Get Times`

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.

The algorithm, described by RUSA: https://rusa.org/pages/acp-brevet-control-times-calculator

The original calculator: https://rusa.org/octime_acp.html

Additional background: https://rusa.org/pages/rulesForRiders
