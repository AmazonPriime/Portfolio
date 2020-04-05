var toggle = true;

function togglePostView() {
    var postTitle = document.getElementById('post_title');
    var postTitleField = document.getElementById('post_title_field');
    var postContent = document.getElementById('post_content');
    var postContentField = document.getElementById('post_content_field');
    var submitButton = document.getElementById('post_submit');

    if (toggle) {
        postTitle.style.display = "none";
        postTitleField.style.display = "initial";
        postContent.style.display = "none";
        postContentField.style.display = "initial";
        submitButton.style.display = "initial";
    } else {
        postTitle.style.display = "initial";
        postTitleField.style.display = "none";
        postContent.style.display = "initial";
        postContentField.style.display = "none";
        submitButton.style.display = "none";
    }

    toggle = !toggle;
}

$('#post_form').on('submit', function(event){
    event.preventDefault();
    updatePost();
});

function updatePost() {
    $.ajax({
        url : this.href,
        type : "POST",
        data : { title : $('#id_title').val() , content : CKEDITOR.instances.id_content.getData()},

        success : function(json) {
            console.log("Successful");
            togglePostView();
            document.getElementById('post_title').innerHTML = json.title;
            document.getElementById('post_content').innerHTML = json.content;
        },

        error : function(xhr,errmsg,err) {
            alert("Blog post exists with this title.");
        }
    });
};


// CODE FOR HANDLING CSRF TOKENS :) 
// https://realpython.com/django-and-ajax-form-submissions/
$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});