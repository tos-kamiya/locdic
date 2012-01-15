<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>LocDic history</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<link rel="stylesheet" href="/static/jquery.mobile-1.0.min.css" />
		<script type="text/javascript" src="/static/jquery-1.7.1.min.js"></script>
		<script type="text/javascript" src="/static/jquery.mobile-1.0.min.js"></script>
	</head>
	<body>
		<div data-role="page" data-theme="d">
			<div data-role="content">
				<h3>{{date}}</h3>
				<table>
					%for word, options, time, ip in history:
					<tr>
						<td>{{word}}</td><td>{{options}}</td><td>{{time}}</td><td>{{ip}}</td>
					</tr>
					%end
				</table>
			</div>
		</div>
	</body>
</html>
