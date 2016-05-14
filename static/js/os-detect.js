function detect()
{
	var os = navigator.userAgent.toString();
	var display = document.getElementById("display");
	display.innerHTML = "OS: " + os;
	var osArray = new Array();
	var i;
	for (i = 0; i < osArray.length; i++)
	{
		if (os.match())
		{
			window.location.replace("http://webpages.charter.net/scuba10steve/html/mobile.html");
		}
	}
}

window.addEventListener("load", detect, false);