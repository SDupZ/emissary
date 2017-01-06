function daysInMonth(month,year) {
    return new Date(year, month + 1, 0).getDate();
}

var totalMonths = 10;

var months = [ "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December" ];

var now = new Date();
var currentYear = now.getFullYear();
var currentMonth = now.getMonth();

var timeData = [];
for (var i = 0; i < totalMonths; i++){
  var date;
  if (currentMonth == 11) {
    date = new Date(currentYear + i, 0, 1, 0, 0, 0, 0);
  } else {
    date = new Date(currentYear, now.getMonth() + i, 1, 0, 0, 0, 0);
  }

  var offset = date.getDay();
  var days =  [];

  for (var j = 0; j < offset; j++){
    days.push({ id: 'id_offset' + j, dayOfMonth: "na", placeholder: true, greyed: false});
  }
  for (var k = 1; k <= daysInMonth(date.getMonth(), date.getFullYear()); k++) {
    days.push({ id: 'id_' + date.getFullYear() + '_' + date.getMonth() + '_' + k, dayOfMonth: k, placeholder: false, value: '' + date.getFullYear() + '_' + date.getMonth() + '_' + k});
  }

  timeData.push({
    year: date.getFullYear(),
    month: months[date.getMonth()],
    days: days,
  });
}

var app = new Vue({
  el: '#app',
  data: {
    daysPerRow: 7,
    timeData: timeData,
    currentMonth: 0,
    totalMonths: totalMonths
  }
});
