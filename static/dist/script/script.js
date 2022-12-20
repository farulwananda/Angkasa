var loadFile = function (event) {
    var reader = new FileReader();
    reader.onload = function () {
        var output = document.getElementById('output');
        output.src = reader.result;
    };

    reader.addEventListener("load", () => {
        localStorage.setItem("recent-image", reader.result);
    });
    reader.readAsDataURL(event.target.files[0]);
};

document.addEventListener("DOMContentLoaded", () => {
    const recentImageDataUrl = localStorage.getItem("recent-image");

    if (recentImageDataUrl) {
        document.querySelector("#output").setAttribute("src", recentImageDataUrl);
    }
});


document.addEventListener("DOMContentLoaded", function (event) {
    var scrollpos = localStorage.getItem("scrollpos");
    if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function (e) {
    localStorage.setItem("scrollpos", window.scrollY);
};


$(document).ready(function () {
    $("input:file").change(function () {
        if ($(this).val()) {
            $("button:submit").attr("disabled", false);
            // or, as has been pointed out elsewhere:
            // $('input:submit').removeAttr('disabled');
        }
    });
});