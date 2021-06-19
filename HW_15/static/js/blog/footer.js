$(document).ready(function () {
    $.ajax({
        method: "GET",
        url: "/footer-items",
        success: function (data) {
            if (data.success) {
                for (let el of data.items) {
                    let footerItemsHtml = "<p>\n" +
                        "                    <a  href=\""+ el.link +"\">" + el.name + "</a>\n" +
                        "             </p>   "
                    $("#footerList").append(footerItemsHtml);
                }
            }
        }
    });
});