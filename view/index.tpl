%if not query_string: query_string = ""
%if not option_wholeword: option_wholeword = 0
%if not option_approximate: option_approximate = 0
%if not option_ignorecase: option_ignorecase = 0
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
					<input type="search" name="query" value="{{query_string}}"/>
					<div class="ui-grid-b">
						<div class="ui-block-a">
							<div data-role="fieldcontain">
							 	<fieldset data-role="controlgroup" data-type="horizontal">
	 								%s = 'checked="checked"' if option_wholeword else ''
									<input type="checkbox" name="wholeword" id="wholeword" class="custom" {{s}} />
									<label for="wholeword">Whole word match</label>
								</fieldset>
							</div>
						</div>
						<div class="ui-block-b">
							<div data-role="fieldcontain">
							    <fieldset data-role="controlgroup" data-type="horizontal">
							    	<label for="approximate" class="select">Mismatch:</label>
									<select name="approximate" id="approximate">
							    		%for v in range(0, 4):
										%s = 'selected="selected"' if option_approximate == v else ''
							         	<option value="{{v}}" {{s}}>{{v}}</option>
							         	%end
									</select>
							    </fieldset>
							</div>
						</div>
						<div class="ui-block-c">
							<div data-role="fieldcontain">
							 	<fieldset data-role="controlgroup" data-type="horizontal">
	 								%s = 'checked="checked"' if option_ignorecase else ''
									<input type="checkbox" name="ignorecase" id="ignorecase" class="custom" {{s}} />
									<label for="ignorecase">Ignore case</label>
								</fieldset>
							</div>
						</div>
					</div>
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
