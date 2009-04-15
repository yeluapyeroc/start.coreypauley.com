/*
 * Global Variables
 */
var basic_commands = null;
var advanced_commands = null;
var bookmarks = null;

$(function() {

        RefreshPage();

        $('body').keypress(function(e) {

            //Enter Key
            if(e.which == 13) {
            query = jQuery.trim($('#query').val()).split(' ');
            query = query.filter(function(x) {
                if(x=="") return false;
                return true
                });
            if(basic_commands) basic_commands = basic_commands.filter(function(x) {
                if(x.fields['command']==query[0]) return true;
                return false;
                });
            if(advanced_commands) advanced_commands = advanced_commands.filter(function(x) {
                if(x.fields['command']==query[0]) return true;
                return false;
                });
            if(bookmarks) bookmarks = bookmarks.filter(function(x) {
                if(x.fields['command']==query[0] && query.length==1) return true;
                return false;
                });
            if(basic_commands[0]) Basic(query, basic_commands[0]);
            if(advanced_commands[0]) Advanced(query, advanced_commands[0]);
            if(bookmarks[0]) Bookmark(bookmarks[0]);
            if(!basic_commands[0] && !advanced_commands[0] && !bookmarks[0]) Google(query);
            }
        });

});

function RefreshPage() {
    $('#query').val('');
    $('#query').focus();

    /*
     * Get JSON data
     */
    $.getJSON("http://" + document.domain + ":8000/basiccommands/", function(json) {
        basic_commands = json;
        });
    $.getJSON("http://" + document.domain + ":8000/advancedcommands/", function(json) {
        advanced_commands = json;
        });
    $.getJSON("http://" + document.domain + ":8000/bookmarks/", function(json) {
        bookmarks = json;
        });
}

function Google(query) {
    var url = 'http://google.com/search?hl=en&q=' + query.join('+') + '&btnG=Google+Search&aq=f&oq=';
    window.location = url;
}

function Basic(query, command) {
    var stub = query.shift();
    var url = command.fields['header1'] + query.join('+') + command.fields['header2'];
    window.location = url;
}

function Advanced(query, command) {
    $.getJSON('http://' + document.domain + ':8000/advanced/' + query.shift() + '/', {'key': query.shift(), 'url': query.shift()}, function(json) {
            if(json['success']){ $('#message').html(json['message']);}
            else{ $('#message').html(json['message']);}
            RefreshPage();
            });
}

function Bookmark(bookmark) {
    window.location = bookmark.fields['url'];
}
