var numberOfTimers = 3;

function getTimeRemaining(endtime){
  var t = Date.parse(endtime) - Date.parse(new Date());
  var secondsRemaining = Math.floor( (t/1000) % 60 );
  var minutesRemaining = Math.floor( (t/1000/60) % 60 );
  var hoursRemaining = Math.floor( (t/(1000*60*60)) % 24 );
  var daysRemaining = Math.floor( t/(1000*60*60*24) );
  return {
    'totalRemaining': t,
    'daysRemaining': daysRemaining,
    'hoursRemaining': hoursRemaining,
    'minutesRemaining': minutesRemaining,
    'secondsRemaining': secondsRemaining
  };
}
var data = {};

var timers = {};
for (i = 0; i < numberOfTimers; i++) {
  var temp = {
    'total': 0,
    'days': 0,
    'hours': 0,
    'minutes': 0,
    'seconds': 0
  }
  data['timer' + i] = temp;
}
var app = new Vue({
  el: '#app',
  data: data
});

function initializeClock(endtime, clockNumber){
  var timeinterval = setInterval(function(){
    var result = getTimeRemaining(endtime);

    app['timer' + clockNumber] = {
      'total': result.totalRemaining,
      'days': result.daysRemaining,

      'hours': result.hoursRemaining,
      'minutes': result.minutesRemaining,
      'seconds': result.secondsRemaining
    }

    if(result.total<=0){
      clearInterval(timeinterval);
    }
  },1000);
}
