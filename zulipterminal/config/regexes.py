# All regexes with (*) are inspired from webapp's
# `static/js/composebox_typeahead.js`


# (*) Example text: #**stream name>Topic name
REGEX_AUTOCOMPLETE_STREAM_TOPIC = r"#\*\*([^*>]+)>([^*]*)$"
# (*) Example text: #**stream name**>Topic name
REGEX_AUTOCOMPLETE_STREAM_TOPIC_FENCED = r"#\*\*([^*>]+)\*\*>([^*]*)$"
