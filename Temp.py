#!/usr/bin/env python

def Template(Problem, Solution, Status):
	ErrorList = ['Message Type', 'AID', 'TYP', 'BCN', 'SPD', 'FIX', 'TIM', 'ALT', 'RTE']
	if(Status == "new"):
		QuestionBox = """<span class="style1">.....</span>Hello, and welcome to my D-CRUD emulator. The sole purpose of this application is to allow you to practice inputting computer messages into a D-CRD similar to the one at the FAA Academy. <BR />
    	<P> <span class="style1">.....</span>There are a couple things you should note. First, this application currently only includes a small set of scenarios to practice. The number of scenarios will, of course, increase with time. However, most importantly, one should note that this program in no way correlates with the logic of the actual D-CRD program. Bear in mind the "error messages" will NOT be identical to what you will see in the actual D-CRD. Also, this emulator may give you error messages that the actual D-CRD would not generate because your input might pass logic tests and still be inaccurate. </P>
   		<P> Hope this helps, my friends.</P>
    	~Joshua Wedekind    """
	else:
		QuestionBox = Problem
	
	print """
		<style type="text/css">
		<!--
	body,td,th {
		font-family: Arial, Helvetica, sans-serif;
		color: #FFFFFF;
	}
	body {
		background-color: #000000;
	}
	.black {
		scrollbar-face-color:#000;
		scrollbar-arrow-color:#000;
		scrollbar-highlight-color:#000;
		scrollbar-shadow-color:#000;
		scrollbar-3dlight-color:#000;
		scrollbar-darkshadow-color:#000;
		scrollbar-track-color:#000;
		background-color: #000000;
		color: #FFFFFF;
		border:0px;
		margin:5px;
		}
	.style1 {color: #000000}
	
	#crd {
		float:left;
		width: 360px;
		}
	#right {
		float:right;
		width: 340px;
		text-align:center;
		}
	#problem {
		border:dashed thin #FFFFFF;
		margin:10px;
		padding:10px;
		text-align:left;
		}
	
	-->
	</style>
	
	<script type="text/javascript">
	
	"""
	
	for i in range(len(Solution)):
		print "var Solution" + str(i+1) + ";"
		print ""
		print "Solution" + str(i+1) + "='" + Solution[i] + "';"
		print ""
		
	print """

var User_answer_orig;
var User_answer;
var crd_response;

function SubmitAnswer(Message_comp) {
	User_answer_orig = Message_comp.value;
	User_answer = Message_comp.value;
	User_answer = User_answer.split(/\s+/);
	
	Field1 = User_answer[0];
	Field2 = User_answer[1];
	Field3 = User_answer[2];
	Field4 = User_answer[3];
	Field5 = User_answer[4];
	Field6 = User_answer[5];
	Field7 = User_answer[6];
	Field8 = User_answer[7];
	Field9 = User_answer[8];
	Field10 = User_answer[9];
	Field11 = User_answer[11];
	
	if(Field1 == "Cal" || Field1 == "CAL" || Field1 == "cal") {
		alert("Uncle Cal!");
		}
	"""
	for j in range(len(Solution)):
		print "else if(Field" + str(j+1) + " != Solution" + str(j+1) + \
		") { document.getElementById('user_message').reset(); document.getElementById('feedback').innerHTML = 'REJECT - " + ErrorList[j] + " ERROR'; } "
	
	print """
	
	else {
		document.getElementById('user_message').reset();
		document.getElementById('feedback').innerHTML = 'ACCEPTED';
		document.getElementById('response_area').innerHTML = '""" + \
		 Solution[1] + " " + Solution[2] + "<BR /> " + Solution[3] \
		+ " " + Solution[4] + " " + Solution[7] + "<BR /> " + Solution[8] \
		+ "';"
	print """
	
		}
	}
	
function submitenter(myfield,e) {
	var keycode;
	if (window.event) keycode = window.event.keyCode;
	else if (e) keycode = e.which;
	else return true;

	if (keycode == 13)
	   {
	   document.user_message.submit()
	   }
	else
	   return true;
	}

</script>

</head>

<body>

<p align="center">D -CRD Emulator. Messaging Input Practice. </p>
<div style="width:800px;">
<div id="crd" align="left">

  <table width="350" border="1" cellspacing="\" cellpadding="1">
    <tr>
      <td height="30"><div align="center">CRD</div></td>
    </tr>
    <tr>
      <td height="30"><div align="center">Message Waiting</div></td>
    </tr>
    <tr>
      <td height="50">&nbsp; ( Hint: use CAPS LOCK )</td>
    </tr>
    <tr>
      <td height="30"><div align="center">Response Area</div></td>
    </tr>
    <tr>
      <td height="80"><div id="response_area">&nbsp;</div></td>
    </tr>
    <tr>
      <td height="30"><div align="center">Message Composition <span class="style1">....................</span>| READY</div></td>
    </tr>
    <tr>
      <td height="110"><form id="user_message" name="user_message" method="post" action="javascript:SubmitAnswer(document.getElementById('Message_comp'))">
        <label>
        <textarea spellcheck="false" class="black" name="Message_comp" id="Message_comp" cols="45" rows="5" onKeyPress="return submitenter(this,event)"></textarea>
        </label>
                                                </form>      </td>
    </tr>
    <tr>
      <td height="60"><div id="feedback">&nbsp;</div></td>
    </tr>
  </table>
</div>

<div id="right">
	<div id="problem">""" + QuestionBox + """
	</div>
    	<input name="Recall" type="button" value="ReCall" onclick="document.getElementById('Message_comp').value = User_answer_orig" />
    	<span class="style1">...................</span>
    	<a href="CRD_Emulator.py?Status=old"><input name="nextproblem" type="button" value="Next Problem -->" ONCLICK="window.location.href='CRD_Emulator.py?Status=old'"/></a> 
</div>

</div>
"""
