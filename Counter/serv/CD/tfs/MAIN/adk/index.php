<!doctype html>
<html>
<head>
	<title>Barcode Scanner</title>
</head>
<style>
table, th, td {
    border: 1px solid black;
	width:auto;
	#height:10px;
	font-size: 12pt;
}
</style>
<body>
<div style = "width:300px;">

	<table style="float:right;">
	<tr>
	<td><b>ADK</b></td>
	</tr>
		<?php
    $db = new SQLite3('/Users/itlabs/db1.db');
	
    $tablesquery = $db->query("SELECT dates,people FROM ADK;");
    while ($table = $tablesquery->fetchArray(SQLITE3_ASSOC)) {
        echo '<tr>';
		#echo '<td>' . $table['Object'] . '<br /></td>';
        echo '<td>' . $table['dates'] . '<br /></td>';
        echo '<td align=\"right\">' . $table['people'] . '<br /><br /></td>';
		echo '</tr>';
	}
	?>
	</table>
	
</div>
	
</body>
</html>