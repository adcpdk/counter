<!doctype html>
<html>
<head>
	<title>TheFaceShop</title>
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
<div	style="width:auto;">
<div style = "#border: 2px solid #FF0000; #width:300px; float:left; margin-right:5px;">

	<table style="border: 2px solid #FF0000;#float:right;">
	<tr>
	<td><b>ADK</b></td>
	<td><b>people</b></td>
	</tr>
		<?php
    $db = new SQLite3('/Users/itlabs/db1.db');
	
    $tablesquery = $db->query("SELECT dates,people FROM adk;");
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
	<div style = "#border: 2px solid #FF0000; #width:300px; float:left; margin-right:5px;">

	<table style="border: 2px solid #FF0000;#float:right;">
	<tr>
	<td><b>Mega</b></td>
	<td><b>people</b></td>
	</tr>
		<?php
    $db = new SQLite3('/Users/itlabs/db1.db');
	
    $tablesquery = $db->query("SELECT dates,people FROM mega;");
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
<div style = "#border: 2px solid #FF0000; #width:300px; float:left; margin-right:5px;">

	<table style="border: 2px solid #FF0000;#float:right;">
	<tr>
	<td><b>Sputnik</b></td>
	<td><b>people</b></td>
	</tr>
		<?php
    $db = new SQLite3('/Users/itlabs/db1.db');
	
    $tablesquery = $db->query("SELECT dates,people FROM sputnik;");
    while ($table = $tablesquery->fetchArray(SQLITE3_ASSOC)) {
        echo '<tr>';
		
        echo '<td>' . $table['dates'] . '<br /></td>';
        echo '<td align=\"right\">' . $table['people'] . '<br /><br /></td>';
		echo '</tr>';
	}
	?>
	</table>
	
</div>
</div>
</body>
</html>