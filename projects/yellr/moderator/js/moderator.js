'use strict';
var moderator = moderator || {};

moderator.main = {
	init: function() {
		// hook up tabs
		document.querySelector('#tabs').onclick = function(e) {
			e.preventDefault();
			if (e.target.nodeName == 'A') {
				console.log(e.target.getAttribute('data-tab'));
				// update current tab
				document.querySelector('#current-tab').id = '';
				e.target.id = 'current-tab';

				// update tab content
				
			}
		};

		// the good shit.
		document.querySelector('#latest-submissions').onclick = function(e) {
			e.preventDefault();
			console.log(e.target);
		}


	}
}


window.onload = function() {
	moderator.main.init();
}