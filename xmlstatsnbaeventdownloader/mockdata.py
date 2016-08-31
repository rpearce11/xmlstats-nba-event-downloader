__author__ = 'Rich Pearce'

#mock from calling: https://erikberg.com/events.json?date=20150614&sport=nba
mockSingleFutureEventData = {
    'events_date': '2015-06-14T00:00:00-04:00',
    'event': [{
        'start_date_time': '2015-06-14T03:45:56-04:00',
        'event_id': '20150614-cleveland-cavaliers-at-golden-state-warriors',
        'away_team': {
            'division': 'Central',
            'full_name': 'Cleveland Cavaliers',
            'conference': 'East',
            'city': 'Cleveland',
            'first_name': 'Cleveland',
            'abbreviation': 'CLE',
            'state': 'Ohio',
            'team_id': 'cleveland-cavaliers',
            'active': True,
            'site_name': 'Quicken Loans Arena',
            'last_name': 'Cavaliers'
        },
        'away_period_scores': [],
        'home_period_scores': [],
        'sport': 'NBA',
        'away_points_scored': -1,
        'site': {
            'name': 'Oracle Arena',
            'city': 'Oakland',
            'surface': 'Hardwood',
            'state': 'California',
            'capacity': 19596
        },
        'event_status': 'scheduled',
        'season_type': 'post',
        'home_points_scored': -1,
        'home_team': {
            'division': 'Pacific',
            'full_name': 'Golden State Warriors',
            'conference': 'West',
            'city': 'Oakland',
            'first_name': 'Golden State',
            'abbreviation': 'GS',
            'state': 'California',
            'team_id': 'golden-state-warriors',
            'active': True,
            'site_name': 'Oracle Arena',
            'last_name': 'Warriors'
        }
    }]
}

#mockData from here: https://erikberg.com/api/endpoints/events
mockTwoEventsData = {
  "events_date" : "2013-01-31T00:00:00-08:00",
  "events_count" : 2,
  "event" : [ {
    "event_id" : "20130131-memphis-grizzlies-at-oklahoma-city-thunder",
    "event_status" : "completed",
    "sport" : "NBA",
    "start_date_time" : "2013-01-31T17:00:00-08:00",
    "season_type" : "regular",
    "away_team" : {
      "team_id" : "memphis-grizzlies",
      "abbreviation" : "MEM",
      "active" : True,
      "first_name" : "Memphis",
      "last_name" : "Grizzlies",
      "conference" : "West",
      "division" : "Southwest",
      "site_name" : "FedExForum",
      "city" : "Memphis",
      "state" : "Tennessee",
      "full_name" : "Memphis Grizzlies"
    },
    "home_team" : {
      "team_id" : "oklahoma-city-thunder",
      "abbreviation" : "OKC",
      "active" : True,
      "first_name" : "Oklahoma City",
      "last_name" : "Thunder",
      "conference" : "West",
      "division" : "Northwest",
      "site_name" : "Chesapeake Energy Arena",
      "city" : "Oklahoma City",
      "state" : "Oklahoma",
      "full_name" : "Oklahoma City Thunder"
    },
    "site" : {
      "capacity" : 19599,
      "surface" : "Hardwood",
      "name" : "Chesapeake Energy Arena",
      "state" : "Oklahoma",
      "city" : "Oklahoma City"
    },
    "away_period_scores" : [ 22, 12, 33, 22 ],
    "home_period_scores" : [ 32, 26, 21, 27 ],
    "away_points_scored" : 89,
    "home_points_scored" : 106
  }, {
    "event_id" : "20130131-dallas-mavericks-at-golden-state-warriors",
    "event_status" : "completed",
    "sport" : "NBA",
    "start_date_time" : "2013-01-31T19:30:00-08:00",
    "season_type" : "regular",
    "away_team" : {
      "team_id" : "dallas-mavericks",
      "abbreviation" : "DAL",
      "active" : True,
      "first_name" : "Dallas",
      "last_name" : "Mavericks",
      "conference" : "West",
      "division" : "Southwest",
      "site_name" : "American Airlines Center",
      "city" : "Dallas",
      "state" : "Texas",
      "full_name" : "Dallas Mavericks"
    },
    "home_team" : {
      "team_id" : "golden-state-warriors",
      "abbreviation" : "GS",
      "active" : True,
      "first_name" : "Golden State",
      "last_name" : "Warriors",
      "conference" : "West",
      "division" : "Pacific",
      "site_name" : "Oracle Arena",
      "city" : "Oakland",
      "state" : "California",
      "full_name" : "Golden State Warriors"
    },
    "site" : {
      "capacity" : 19596,
      "surface" : "Hardwood",
      "name" : "Oracle Arena",
      "state" : "California",
      "city" : "Oakland"
    },
    "away_period_scores" : [ 23, 30, 26, 18 ],
    "home_period_scores" : [ 28, 27, 25, 20 ],
    "away_points_scored" : 97,
    "home_points_scored" : 100
  } ]
}

#single event Mock Data
mockSingleEventData = {
  "events_date" : "2013-01-31T00:00:00-08:00",
  "events_count" : 1,
  "event" : [ {
    "event_id" : "20130131-memphis-grizzlies-at-oklahoma-city-thunder",
    "event_status" : "completed",
    "sport" : "NBA",
    "start_date_time" : "2013-01-31T17:00:00-08:00",
    "season_type" : "regular",
    "away_team" : {
      "team_id" : "memphis-grizzlies",
      "abbreviation" : "MEM",
      "active" : True,
      "first_name" : "Memphis",
      "last_name" : "Grizzlies",
      "conference" : "West",
      "division" : "Southwest",
      "site_name" : "FedExForum",
      "city" : "Memphis",
      "state" : "Tennessee",
      "full_name" : "Memphis Grizzlies"
    },
    "home_team" : {
      "team_id" : "oklahoma-city-thunder",
      "abbreviation" : "OKC",
      "active" : True,
      "first_name" : "Oklahoma City",
      "last_name" : "Thunder",
      "conference" : "West",
      "division" : "Northwest",
      "site_name" : "Chesapeake Energy Arena",
      "city" : "Oklahoma City",
      "state" : "Oklahoma",
      "full_name" : "Oklahoma City Thunder"
    },
    "site" : {
      "capacity" : 19599,
      "surface" : "Hardwood",
      "name" : "Chesapeake Energy Arena",
      "state" : "Oklahoma",
      "city" : "Oklahoma City"
    },
    "away_period_scores" : [ 22, 12, 33, 22 ],
    "home_period_scores" : [ 32, 26, 21, 27 ],
    "away_points_scored" : 89,
    "home_points_scored" : 106
  }]
}
