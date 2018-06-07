//テキストボックスの文字を取得する
function tbox1(){
  /*var str=document.js.txtb.value;
  str = "&lt;p&gt;"+"<br>"+str;
  str = str.replace(/\n/g, "<br>"+"&lt;/p&gt;"+"<br>"+"&lt;p&gt;"+"<br>");
  str = str+"<br>"+"&lt;/p&gt;";*/

  //alert(str);
  //var space = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
  //str = space + "&lt;pre&nbsp;class=&quot;box-code&quot;&gt;\n" + str + "&lt;/pre&gt;"
  //str = "<pre id=&quot;result&quot;>" + str + "</pre>";

  var form = document.getElementsByName("js")[0];
  //form.insertAdjacentHTML('afterend', str);
  //----------------------------------------------------

  //CR+LF,CR,LF のいずれかの改行コードでsplitします。
  var text = document.js.txtb.value;
  var textArray = text.split(/\r\n|\r|\n/);
  //これでtextArrayの中身は["おはよう。","こんにちは。","こんばんは"]になります。

  var flag = false;
  for (var i = 0; i < textArray.length; i++) {
    if (textArray[i].match(/\/pre/)) {
      textArray[i] = space_lt_gt(textArray[i]);
      flag = false;

    } else if (textArray[i].match(/pre class="box-code"/)) {//preのみだと△?
      textArray[i] = space_lt_gt(textArray[i]);
      flag = true;

    } else if (flag == false) {
      textArray[i] = textArray[i].replace(/&lt;/g, "&amp;amp;lt;");//不要?
      textArray[i] = textArray[i].replace(/&gt;/g, "&amp;amp;gt;");//不要?
      textArray[i] = textArray[i].replace(/</g, "&amp;lt;");
      textArray[i] = textArray[i].replace(/>/g, "&amp;gt;");
      var spaces = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+"&nbsp;&nbsp;";
      var before = spaces+"&lt;p&gt;"+"<br>";
      var after = spaces+"&lt;/p&gt;"+"<br>";
      textArray[i] = before+spaces+"&nbsp;&nbsp;"+textArray[i]+"<br>"+after;
      
    } else {
      textArray[i] = space_lt_gt(textArray[i]);

    }
  }
  
  var new_text = "";
  //new_text = "&lt;p&gt;"+"<br>";
  for (var i = 0; i < textArray.length; i++) {
    new_text = new_text+textArray[i];
    //+"<br>";
  }
  //new_text = new_text+"<br>"+"&lt;/p&gt;";
  new_text = '<pre id="result" class="temp">' + new_text + "</pre>";

  form.insertAdjacentHTML('afterend', new_text);

}


//テキストボックスの文字を操作する
function clr(){
  document.js.txtb.value="";

  //var res = document.getElementById("result");
  var results = document.getElementsByClassName("temp");
  //results.forEach(function( result ) {
  //昇順にけすとうまくいかない
  //9個->[0]消す->次は8個のうちの[1]->...1/2くらいにしかならない
  //Array.prototype.forEach.call(results, function(value, index, result) {
  for (var i = results.length-1; i >= 0; i--) {
    results[i].outerHTML = "";
    //alert(index);
  }

  //window.location.reload();
}

function space_lt_gt(text){
      text = text.replace(/\ /g, "&nbsp;");//スペース
      text = text.replace(/&lt;/g, "&amp;lt;");
      text = text.replace(/&gt;/g, "&amp;gt;");
      text = text.replace(/</g, "&lt;");
      text = text.replace(/>/g, "&gt;");

      /*
      //<pre class="box-code">, </pre>をもとに戻す
      if (text.match(/&amp;lt;pre\ class=&quot;box-code&quot;&amp;gt;/)) {
        alert(text);
        //text = text.replace(/&amp;lt;pre\ class="box-code"&amp;gt;/g, "&lt;pre class=&quot;box-code&quot;&gt;");
      }
      //&lt;pre class="box-code"&gt;
      text = text.replace(/&amp;lt;\/pre&amp;gt;/g, "&lt;/pre&gt;");
      */

      text = text+"<br>";
      return text;
}