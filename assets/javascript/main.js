// Bootstrap requres specific capitalization (and order of imports) for jQuery and Tether
global.jQuery = require('jquery');
global.Tether = require('tether');
require('bootstrap');

var $ = global.jQuery;
window.$ = $;

require('./ticket_list');
