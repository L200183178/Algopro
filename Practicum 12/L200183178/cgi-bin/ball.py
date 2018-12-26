def ball():
    volume = 4.19*7**3
    return volume
print "<!DOCTYPE html>"
print
print """<html>
	<head>
		<title>Ball Volume</title>
	</head>
	<body>
		<form>
			<table>
				<tr>
					<td rowspan='8'>
					<img src='../ball.jpg' width='160' height='160'>
					</td>
					<td>
						<p><b><font size='5'>Geometry</font></b></p>
					</td>
				</tr>
				
				<tr>
					<td>Shape</td>
					<td>:</td>
					<td>Ball</td>
				</tr>
				
				<tr>
					<td>Dimension</td>
					<td>:</td>
					<td>3D</td>
				</tr>
				
				<tr>
					<td>Volume Formula</td>
					<td>:</td>
					<td>4/3 x phi x radius</td>
				</tr>
				
				<tr>
					<td>Radius</td>
					<td>:</td>
					<td>
					7
					</td>
				</tr>
				
    
				<tr>
					<td>Volume</td>
					<td>:</td>
					<td>"""
print ball()
print"""</td>
				</tr>
			</table>
		</form>
	</body>
</html>"""