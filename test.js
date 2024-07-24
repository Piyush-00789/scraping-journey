var FormData = require('form-data');
var XMLHttpRequest = require('xhr2');

var fs = require('fs');
var data = new FormData();
data.append("view_name", "members_listing");
data.append("view_display_id", "page_1");
data.append("view_path", "members-listing/w");
data.append("view_base_path", "members-listing");
data.append("view_dom_id", "e80369798acdf78ad15978259a42e21ef6a498e3c5f3b7ed41e141ce19184592");
data.append("pager_element", "0");
data.append("page", "2");
data.append("_drupal_ajax", "1");
data.append("view_args", "w");

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "https://nasscom.in/views/ajax?_wrapper_format=drupal_ajax");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.setRequestHeader("Origin", "https://nasscom.in");
xhr.setRequestHeader("Referer", "https://nasscom.in/members-listing");
xhr.setRequestHeader("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36");
xhr.setRequestHeader("Cookie", "sess_map=brafyeeyreuterervdtzyezwawyaweavufezuqsydyvzwtccbqbqvyexsfyarauyxfesresqubfzdfuqceaubbauezwccwyasaydsbaedxcszfcdrxqqxwtvveddaqucutdudrwwswdqwvrvruqcayfv");

xhr.send(data);