import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

sender =  os.getenv("SENDER")
password = os.getenv("PASSWORD")
reciver  = ""

message  = MIMEMultipart()
message["From"] = sender
message["To"] = reciver
message["Subject"]  = "Hello again"

body = """
<!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0"><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<style>
		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			padding: 0;
		}

		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: inherit !important;
		}

		#MessageViewBody a {
			color: inherit;
			text-decoration: none;
		}

		p {
			line-height: inherit
		}

		.desktop_hide,
		.desktop_hide table {
			mso-hide: all;
			display: none;
			max-height: 0px;
			overflow: hidden;
		}

		.image_block img+div {
			display: none;
		}

		sup,
		sub {
			line-height: 0;
			font-size: 75%;
		}

		#converted-body .list_block ul,
		#converted-body .list_block ol,
		.body [class~="x_list_block"] ul,
		.body [class~="x_list_block"] ol,
		u+.body .list_block ul,
		u+.body .list_block ol {
			padding-left: 20px;
		}

		.menu_block.desktop_hide .menu-links span {
			mso-hide: all;
		}

		@media (max-width:740px) {

			.desktop_hide table.icons-inner,
			.social_block.desktop_hide .social-table {
				display: inline-block !important;
			}

			.icons-inner {
				text-align: center;
			}

			.icons-inner td {
				margin: 0 auto;
			}

			.image_block div.fullWidth {
				max-width: 100% !important;
			}

			.menu-checkbox[type=checkbox]~.menu-links {
				display: none !important;
				padding: 5px 0;
			}

			.menu-checkbox[type=checkbox]:checked~.menu-trigger .menu-open {
				display: none !important;
			}

			.menu-checkbox[type=checkbox]:checked~.menu-links,
			.menu-checkbox[type=checkbox]~.menu-trigger {
				display: block !important;
				max-width: none !important;
				max-height: none !important;
				font-size: inherit !important;
			}

			.menu-checkbox[type=checkbox]~.menu-links>a,
			.menu-checkbox[type=checkbox]~.menu-links>span.label {
				display: block !important;
				text-align: center;
			}

			.menu-checkbox[type=checkbox]:checked~.menu-trigger .menu-close {
				display: block !important;
			}

			.mobile_hide {
				display: none;
			}

			.row-content {
				width: 100% !important;
			}

			.stack .column {
				width: 100%;
				display: block;
			}

			.mobile_hide {
				min-height: 0;
				max-height: 0;
				max-width: 0;
				overflow: hidden;
				font-size: 0px;
			}

			.desktop_hide,
			.desktop_hide table {
				display: table !important;
				max-height: none !important;
			}
		}

		#memu-r1c1m1:checked~.menu-links {
			background-color: #00d09c !important;
		}

		#memu-r1c1m1:checked~.menu-links a,
		#memu-r1c1m1:checked~.menu-links span {
			color: #ffffff !important;
		}
	</style><!--[if mso ]><style>sup, sub { font-size: 100% !important; } sup { mso-text-raise:10% } sub { mso-text-raise:-10% }</style> <![endif]-->
</head>

<body class="body" style="margin: 0; background-color: #ffffff; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:25px;line-height:25px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:25px;padding-top:10px;width:100%;padding-right:0px;">
																<div class="alignment" align="left" style="line-height:10px">
																	<div style="max-width: 180px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/Job_logo.png" style="display: block; height: auto; border: 0; width: 100%;" width="180" alt="Alternate text" title="Alternate text" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
													<table class="menu_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="color:#393d47;font-family:inherit;font-size:16px;padding-right:20px;text-align:right;">
																<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																	<tr>
																		<td class="alignment" style="text-align:right;font-size:0px;"><!--[if !mso]><!--><input class="menu-checkbox" id="memu-r1c1m1" type="checkbox" style="display:none !important;max-height:0;visibility:hidden;"><!--<![endif]-->
																			<div class="menu-trigger" style="display:none;max-height:0px;max-width:0px;font-size:0px;overflow:hidden;"><label class="menu-label" for="memu-r1c1m1" style="height: 36px; width: 36px; display: inline-block; cursor: pointer; mso-hide: all; user-select: none; align: right; text-align: center; color: #ffffff; text-decoration: none; background-color: #00d09c; border-radius: 50%;"><span class="menu-open" style="word-break: break-word; mso-hide: all; font-size: 26px; line-height: 31.5px;">☰</span><span class="menu-close" style="word-break: break-word; display: none; mso-hide: all; font-size: 26px; line-height: 36px;">✕</span></label></div>
																			<div class="menu-links"><!--[if mso]><table role="presentation" border="0" cellpadding="0" cellspacing="0" align="right" style=""><tr style="text-align:right;"><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:20px;padding-bottom:5px;padding-left:15px"><![endif]--><span class="label" style="word-break: break-word; mso-hide: false; padding-top: 5px; padding-bottom: 5px; padding-left: 15px; padding-right: 20px; display: inline; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; color: false; letter-spacing: normal;">Log In</span><!--[if mso]></td><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:20px;padding-bottom:5px;padding-left:15px"><![endif]--><span class="label" style="word-break: break-word; mso-hide: false; padding-top: 5px; padding-bottom: 5px; padding-left: 15px; padding-right: 20px; display: inline; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; color: false; letter-spacing: normal;">Find Job</span><!--[if mso]></td><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:20px;padding-bottom:5px;padding-left:15px"><![endif]--><span class="label" style="word-break: break-word; mso-hide: false; padding-top: 5px; padding-bottom: 5px; padding-left: 15px; padding-right: 20px; display: inline; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; color: false; letter-spacing: normal;">Post a Job</span><!--[if mso]></td><![endif]--><!--[if mso]></tr></table><![endif]--></div>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-3" style="height:25px;line-height:25px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-3" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; background-position: top center; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
													<table class="paragraph_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:25px;padding-right:25px;padding-top:10px;">
																<div style="color:#1f0b0b;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:38px;line-height:120%;text-align:left;mso-line-height-alt:45.6px;">
																	<p style="margin: 0; word-break: break-word;"><span style="word-break: break-word;"><strong><span style="word-break: break-word;">We're happy</span></strong></span></p>
																	<p style="margin: 0; word-break: break-word;"><span style="word-break: break-word;"><strong><span style="word-break: break-word;">you're here.</span></strong></span></p>
																</div>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:25px;padding-left:25px;padding-right:25px;padding-top:10px;">
																<div style="color:#393d47;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:14px;line-height:180%;text-align:left;mso-line-height-alt:25.2px;">
																	<p style="margin: 0; word-break: break-word;">Digital and all-encompassing recruitment services tailored to your needs</p>
																</div>
															</td>
														</tr>
													</table>
													<table class="button_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:10px;padding-top:10px;text-align:left;">
																<div class="alignment" align="left"><!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" style="height:52px;width:230px;v-text-anchor:middle;" arcsize="8%" stroke="false" fillcolor="#00d09c">
<w:anchorlock/>
<v:textbox inset="5px,0px,0px,0px">
<center dir="false" style="color:#ffffff;font-family:Tahoma, sans-serif;font-size:16px">
<![endif]-->
																	<div style="background-color:#00d09c;border-bottom:0px solid #8a3b8f;border-left:0px solid #8a3b8f;border-radius:4px;border-right:0px solid #8a3b8f;border-top:0px solid #8a3b8f;color:#ffffff;display:inline-block;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:16px;font-weight:undefined;mso-border-alt:none;padding-bottom:10px;padding-top:10px;text-align:center;text-decoration:none;width:auto;word-break:keep-all;"><span style="word-break: break-word; padding-left: 50px; padding-right: 45px; font-size: 16px; display: inline-block; letter-spacing: normal;"><span style="word-break: break-word; line-height: 32px;"><strong>Find Your Talent</strong></span></span></div><!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
													<table class="image_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-right:5px;width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 355px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/first_imag.png" style="display: block; height: auto; border: 0; width: 100%;" width="355" alt="Alternate text" title="Alternate text" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-3" style="height:40px;line-height:40px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-4 mobile_hide" style="height:40px;line-height:40px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-4" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #e4faf4;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
													<table class="paragraph_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:35px;padding-right:35px;padding-top:5px;">
																<div style="color:#34495e;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:20px;line-height:150%;text-align:center;mso-line-height-alt:30px;">
																	<p style="margin: 0; word-break: break-word;"><span style="word-break: break-word;"><strong><span style="word-break: break-word;">Trusted by Millions of People</span></strong></span></p>
																</div>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-3 mobile_hide" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1 mobile_hide" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-2 mobile_hide" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
													<table class="image_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:15px;padding-left:15px;padding-right:15px;width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 330px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/logoos.png" style="display: block; height: auto; border: 0; width: 100%;" width="330" alt="Alternate text" title="Alternate text" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-4" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-5" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:40px;line-height:40px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-6" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; background-position: center top;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center" style="line-height:10px">
																	<div class="fullWidth" style="max-width: 340px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/Guy_computer.png" style="display: block; height: auto; border: 0; width: 100%;" width="340" alt="Alternate text" title="Alternate text" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1 mobile_hide" style="height:50px;line-height:50px;font-size:1px;">&#8202;</div>
													<table class="paragraph_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:25px;padding-right:25px;">
																<div style="color:#34495e;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:24px;line-height:200%;text-align:left;mso-line-height-alt:48px;">
																	<p style="margin: 0; word-break: break-word;"><span style="word-break: break-word;"><strong>Direct Search Services</strong></span></p>
																</div>
															</td>
														</tr>
													</table>
													<table class="list_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word; color: #555555; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 14px; line-height: 200%; text-align: left; mso-line-height-alt: 28px;">
														<tr>
															<td class="pad" style="padding-bottom:5px;padding-left:45px;padding-right:25px;">
																<div style="margin-left:-20px">
																	<ul style="margin-top: 0; margin-bottom: 0; list-style-type: revert;">
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Hourly-Based Recruitment Support</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Digital Headhunting</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Direct Search Services</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Employer Branding</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Outsourced Recruitment</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Big Data Search Technology</li>
																	</ul>
																</div>
															</td>
														</tr>
													</table>
													<table class="button_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:25px;padding-right:10px;padding-top:10px;text-align:left;">
																<div class="alignment" align="left"><!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" style="height:52px;width:189px;v-text-anchor:middle;" arcsize="8%" stroke="false" fillcolor="#00d09c">
<w:anchorlock/>
<v:textbox inset="5px,0px,0px,0px">
<center dir="false" style="color:#ffffff;font-family:Tahoma, sans-serif;font-size:16px">
<![endif]-->
																	<div style="background-color:#00d09c;border-bottom:0px solid #8a3b8f;border-left:0px solid #8a3b8f;border-radius:4px;border-right:0px solid #8a3b8f;border-top:0px solid #8a3b8f;color:#ffffff;display:inline-block;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:16px;font-weight:undefined;mso-border-alt:none;padding-bottom:10px;padding-top:10px;text-align:center;text-decoration:none;width:auto;word-break:keep-all;"><span style="word-break: break-word; padding-left: 50px; padding-right: 45px; font-size: 16px; display: inline-block; letter-spacing: normal;"><span style="word-break: break-word; line-height: 32px;"><strong>Get Started</strong></span></span></div><!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-7" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:50px;line-height:50px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-8" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/Background_green.png'); background-repeat: no-repeat;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1 mobile_hide" style="height:65px;line-height:65px;font-size:1px;">&#8202;</div>
													<table class="paragraph_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:25px;padding-right:25px;">
																<div style="color:#34495e;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:24px;line-height:200%;text-align:left;mso-line-height-alt:48px;">
																	<p style="margin: 0; word-break: break-word;"><span style="word-break: break-word;"><strong>Outsourced recruitment</strong></span></p>
																</div>
															</td>
														</tr>
													</table>
													<table class="list_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word; color: #555555; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 14px; line-height: 200%; text-align: left; mso-line-height-alt: 28px;">
														<tr>
															<td class="pad" style="padding-bottom:5px;padding-left:45px;padding-right:25px;">
																<div style="margin-left:-20px">
																	<ul style="margin-top: 0; margin-bottom: 0; list-style-type: revert;">
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Hourly-Based Recruitment Support</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Digital Headhunting</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Direct Search Services</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Employer Branding</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Outsourced Recruitment</li>
																		<li style="word-break: break-word; Margin: 0 0 0 0;">Big Data Search Technology</li>
																	</ul>
																</div>
															</td>
														</tr>
													</table>
													<table class="button_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:25px;padding-right:10px;padding-top:10px;text-align:left;">
																<div class="alignment" align="left"><!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" style="height:52px;width:189px;v-text-anchor:middle;" arcsize="8%" stroke="false" fillcolor="#00d09c">
<w:anchorlock/>
<v:textbox inset="5px,0px,0px,0px">
<center dir="false" style="color:#ffffff;font-family:Tahoma, sans-serif;font-size:16px">
<![endif]-->
																	<div style="background-color:#00d09c;border-bottom:0px solid #8a3b8f;border-left:0px solid #8a3b8f;border-radius:4px;border-right:0px solid #8a3b8f;border-top:0px solid #8a3b8f;color:#ffffff;display:inline-block;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:16px;font-weight:undefined;mso-border-alt:none;padding-bottom:10px;padding-top:10px;text-align:center;text-decoration:none;width:auto;word-break:keep-all;"><span style="word-break: break-word; padding-left: 50px; padding-right: 45px; font-size: 16px; display: inline-block; letter-spacing: normal;"><span style="word-break: break-word; line-height: 32px;"><strong>Get Started</strong></span></span></div><!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
																</div>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-5" style="height:35px;line-height:35px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1 mobile_hide" style="height:55px;line-height:55px;font-size:1px;">&#8202;</div>
													<table class="image_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center" style="line-height:10px">
																	<div class="fullWidth" style="max-width: 340px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/Guy_texting.png" style="display: block; height: auto; border: 0; width: 100%;" width="340" alt="Alternate text" title="Alternate text" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-9" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-2" style="height:45px;line-height:45px;font-size:1px;">&#8202;</div>
													<table class="paragraph_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:35px;padding-right:35px;padding-top:5px;">
																<div style="color:#34495e;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:24px;line-height:150%;text-align:center;mso-line-height-alt:36px;">
																	<p style="margin: 0; word-break: break-word;"><strong><span style="word-break: break-word;">Manage your recruitment&nbsp; from your hand.</span></strong></p>
																</div>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:25px;padding-left:25px;padding-right:25px;padding-top:10px;">
																<div style="color:#393d47;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:14px;line-height:180%;text-align:center;mso-line-height-alt:25.2px;">
																	<p style="margin: 0; word-break: break-word;">Digital and all-encompassing recruitment services tailored to your needs</p>
																</div>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:35px;padding-right:35px;padding-top:5px;">
																<div style="color:#34495e;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:24px;line-height:150%;text-align:center;mso-line-height-alt:36px;">
																	<p style="margin: 0; word-break: break-word;"><strong><span style="word-break: break-word;">Download the App now</span></strong></p>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-10" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-2" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:15px;width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 160px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/App_Store_Badge_US_Black.png" style="display: block; height: auto; border: 0; width: 100%;" width="160" alt="Alternate text" title="Alternate text" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-2" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-3" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:15px;width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 160px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/Google_Play_Badge_US.png" style="display: block; height: auto; border: 0; width: 100%;" width="160" alt="Alternate text" title="Alternate text" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-2" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-4" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1 mobile_hide" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-11" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1831/Bottom_section.png'); background-position: center top; background-repeat: no-repeat;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:55px;line-height:55px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-2" style="height:55px;line-height:55px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-3" style="height:55px;line-height:55px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-12" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:55px;line-height:55px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-13" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="paragraph_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:10px;padding-top:10px;">
																<div style="color:#00d09c;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:16px;line-height:120%;text-align:left;mso-line-height-alt:19.2px;">
																	<p style="margin: 0; word-break: break-word;"><strong>&nbsp;Quick Links</strong></p>
																</div>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:10px;padding-top:10px;">
																<div style="color:#393d47;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:14px;line-height:180%;text-align:left;mso-line-height-alt:25.2px;">
																	<p style="margin: 0; word-break: break-word;"><a style="text-decoration: none; color: #393d47;" href="#" target="_blank" rel="noopener">Latest Job</a></p>
																	<p style="margin: 0; word-break: break-word;"><a style="text-decoration: none; color: #393d47;" href="#" target="_blank" rel="noopener">Help Center</a></p>
																	<p style="margin: 0; word-break: break-word;"><a style="text-decoration: none; color: #393d47;" href="#" target="_blank" rel="noopener">Tour Guide</a></p>
																	<p style="margin: 0; word-break: break-word;"><a style="text-decoration: none; color: #393d47;" href="#" target="_blank" rel="noopener">FAQ's</a></p>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="paragraph_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#00d09c;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:16px;line-height:120%;text-align:left;mso-line-height-alt:19.2px;">
																	<p style="margin: 0; word-break: break-word;"><strong>Contact Info</strong></p>
																</div>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#393d47;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:14px;line-height:180%;text-align:left;mso-line-height-alt:25.2px;">
																	<p style="margin: 0; word-break: break-word;">UK (+23) 456 7890&nbsp;<br>US (+22) 456 7891</p>
																	<p style="margin: 0; word-break: break-word;">&nbsp;</p>
																	<p style="margin: 0; word-break: break-word;">support@domain.com&nbsp;<br>sales@domain.com</p>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-3" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="paragraph_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#00d09c;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:16px;line-height:120%;text-align:left;mso-line-height-alt:19.2px;">
																	<p style="margin: 0; word-break: break-word;"><strong>Company Name</strong></p>
																</div>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#393d47;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:14px;line-height:180%;text-align:left;mso-line-height-alt:25.2px;">
																	<p style="margin: 0; word-break: break-word;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sed&nbsp;</p>
																</div>
															</td>
														</tr>
													</table>
													<table class="social_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="left">
																	<table class="social-table" width="144px" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;">
																		<tr>
																			<td style="padding:0 4px 0 0;"><a href="https://www.facebook.com" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-dark-gray/facebook@2x.png" width="32" height="auto" alt="Facebook" title="Facebook" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 4px 0 0;"><a href="https://www.twitter.com" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-dark-gray/twitter@2x.png" width="32" height="auto" alt="Twitter" title="Twitter" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 4px 0 0;"><a href="https://www.instagram.com" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-dark-gray/instagram@2x.png" width="32" height="auto" alt="Instagram" title="Instagram" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 4px 0 0;"><a href="https://www.linkedin.com" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-dark-gray/linkedin@2x.png" width="32" height="auto" alt="LinkedIn" title="LinkedIn" style="display: block; height: auto; border: 0;"></a></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-14" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:55px;line-height:55px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-15" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #ffffff; width: 720px; margin: 0 auto;" width="720">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: center; line-height: 0;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #1e0e4b; font-family: 'Inter', sans-serif; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;"><!--[if vml]><table align="center" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																<!--[if !vml]><!-->
																<table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation"><!--<![endif]-->
																	<tr>
																		<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 6px;"><a href="http://designedwithbeefree.com/" target="_blank" style="text-decoration: none;"><img class="icon" alt="Beefree Logo" src="https://d1oco4z2z1fhwp.cloudfront.net/assets/Beefree-logo.png" height="auto" width="34" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></a></td>
																		<td style="font-family: 'Inter', sans-serif; font-size: 15px; font-weight: undefined; color: #1e0e4b; vertical-align: middle; letter-spacing: undefined; text-align: center; line-height: normal;"><a href="http://designedwithbeefree.com/" target="_blank" style="color: #1e0e4b; text-decoration: none;">Designed with Beefree</a></td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>

</html>
"""
mimetext = MIMEText(body, "html")
message.attach(mimetext)
# send attachment with html email
attachment_path = "emails.csv"
attachment_file = open(attachment_path,"rb")
payload = MIMEBase("application", "octate-stream")
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header("Content-Disposition", "attachment",filename=attachment_path)
message.attach(payload)

server = smtplib.SMTP("smtp.office365.com",587)
server.starttls()
server.login(sender, password)
message_text =  message.as_string()
server.sendmail(sender,reciver,message_text)
server.quit()
