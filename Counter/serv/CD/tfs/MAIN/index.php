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
	<td>ADK</td>
	</tr>
		<?php
    $db = new SQLite3('/Users/itlabs/db1.db');
	
    $tablesquery = $db->query("SELECT Date,Count FROM ADK;");
    while ($table = $tablesquery->fetchArray(SQLITE3_ASSOC)) {
        echo '<tr>';
		#echo '<td>' . $table['Object'] . '<br /></td>';
        echo '<td>' . $table['Date'] . '<br /></td>';
        echo '<td align=\"right\">' . $table['Count'] . '<br /><br /></td>';
		echo '</tr>';
	}
	?>
	</table>
	<table style="float:right;">
	<tr>
	<td>Sputnik</td>
	</tr>
		<?php
    $db = new SQLite3('/Users/itlabs/db1.db');
	
    $tablesquery = $db->query("SELECT Date,Count FROM Sputnik;");
    while ($table = $tablesquery->fetchArray(SQLITE3_ASSOC)) {
        echo '<tr>';
        echo '<td>' . $table['Date'] . '<br /></td>';
        echo '<td align=\"right\">' . $table['Count'] . '<br /><br /></td>';
		echo '</tr>';
	}
	?>
	</table>
	<table style="">
	<tr>
	<td>MEGA</td>
	</tr>
		<?php
    $db = new SQLite3('/Users/itlabs/db1.db');
	
    $tablesquery = $db->query("SELECT Date,Count FROM MEGA;");
    while ($table = $tablesquery->fetchArray(SQLITE3_ASSOC)) {
        echo '<tr>';
        echo '<td>' . $table['Date'] . '<br /></td>';
        echo '<td align=\"right\">' . $table['Count'] . '<br /><br /></td>';
		echo '</tr>';
	}
	?>
	</table>
</div>
	
</body>
</html>