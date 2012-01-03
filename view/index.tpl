<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>LocDic</title>
		<style>
			.dictionaryTitle {
				background-color: #a0a0a0;
			}
			.evenRow {
				background-color: #f0f0ff
			}
			.oddRow {
				background-color: #ffffff
			}
		</style>
	</head>
	<body>
		<form method="post">
			%if not query_string: query_string = ""
			<input type="text" name="query" value="{{query_string}}"/>
			<input type="submit" value="search" />
		</form>
		<div id="result">
			%if not result_table: result_table = {}
			%for dictionary, lines in sorted(result_table.iteritems()):
				<div class="dictionaryTitle">
					{{dictionary}}
				</div>
				<table>
					%for li, L in enumerate(lines):
						%fields = L.split('\t')
						%fields = ["%d" % (li + 1)] + fields
						%rowClass = "evenRow" if li % 2 == 1 else "oddRow"
						<tr class="{{rowClass}}">
							%for f in fields: 
								<td>{{f}}</td>
							%end
						</tr>
					%end
				</table>
			%end
		</div>
	</body>
</html>
