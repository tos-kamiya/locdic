<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<link rel="stylesheet" href="/static/jquery.mobile-1.0.min.css" />
		<script type="text/javascript" src="/static/jquery-1.7.1.min.js"></script>
		<script type="text/javascript" src="/static/jquery.mobile-1.0.min.js"></script>
		<title>LocDic</title>
	</head>
	<body>
		<div data-role="page" data-theme="d">
			<div data-role="content">
				<form method="post">
					%if not query_string: query_string = ""
					<input type="search" name="query" value="{{query_string}}"/>
					<input data-role="button" data-inline="true" type="submit" value="search" />
				</form>
				<div id="result">
					%if not result_table: result_table = {}
					%for dictionary, lines in sorted(result_table.iteritems()):
					<div data-role="collapsible" data-content-theme="d" data-collapsed="false">
						<h3>{{dictionary}}</h3>
						<table>
							%for li, L in enumerate(lines):
							%fields = L.split('\t')
							%fields = ["%d" % (li + 1)] + fields
							<tr>
								%for f in fields: 
									<td>{{f}}</td>
								%end
							</tr>
							%end
						</table>
					</div>
					%end
				</div>
			</div>
		</div>
	</body>
</html>
