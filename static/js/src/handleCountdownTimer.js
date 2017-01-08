// var deadline = '';

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

var app = new Vue({
  el: '#app',
  data: {
    'total': 0,
    'days': 0,
    'hours': 0,
    'minutes': 0,
    'seconds': 0
  }
});

function initializeClock(endtime){
  var timeinterval = setInterval(function(){
    var result = getTimeRemaining(endtime);
    app.total = result.totalRemaining;
    app.days = result.daysRemaining;
    app.hours = result.hoursRemaining
    app.minutes = result.minutesRemaining;
    app.seconds = result.secondsRemaining;

    if(result.total<=0){
      clearInterval(timeinterval);
    }
  },1000);
}

//initializeClock(deadline);
