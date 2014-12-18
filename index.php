<!DOCTYPE html> 

<html>

	<head>

		<meta charset="UTF-8" />
		<meta name="author" content="Dan Marzin" />
		<meta name="copyright" content="" />
		<meta name="robots" content="index, follow" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />

		<title>Rowan Time Sheet PDF Generator</title>

		<link rel="Shortcut Icon" href="favicon.ico" type="image/x-icon" />
		<!--<link rel="stylesheet" href="css/print.css" type="text/css" media="print" />
		<link rel="stylesheet" href="css/screen.css" type="text/css" media="screen,projection" />-->
		<link rel="index" title="" href="" />

		<!--[if lt IE 9 ]>
			<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
		<![endif]--> 

		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js"></script>

	</head>

	<body class="" lang="en-US">

		<!--<header id="primary-header">

			<nav id="primary-navigation">
				<ul>
					<li><a href="" title=""></a></li>
				</ul>
			</nav>

		</header>

		<div id="content-wrapper">

			<aside id="left">
				<nav id="contextual-navigation">
					<ul>
						<li><a href="" title=""></a></li>
					</ul>
				</nav>
			</aside>

			<section id="content">
			</section>

			<aside id="right">
			</aside>

		</div>-->
		<form action="run_python.php" method="post" enctype="multipart/form-data">
			<ul>
                <li>
                    Pay Period Number:
                    <input type="text" name="PayPeriod">
                </li>
				<li>
					Start Date:
					<input type="date" name="Date"/>

					<script>
					    if (!Modernizr.touch || !Modernizr.inputtypes.date) {
					        $('input[type=date]')
					            .attr('type', 'text')
					            .datepicker({
					                // Consistent format with the HTML5 picker
					                dateFormat: 'yy-mm-dd'
					            });
					    }
					</script>
				</li>
				<li>
					<input type="file" name="Name"/>
				</li>
				<li>
					<button type="submit">Create</button>
				</li>
		</form>





		<footer>
		</footer>

	</body>

</html>
