// Browserify master list of js imports
global.jQuery = require('jquery');
global.Popper = require('popper.js');
require('bootstrap');


var $ = global.jQuery;
window.$ = $;

require('./ticket_list');
