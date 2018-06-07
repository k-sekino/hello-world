//テキストボックスの文字を取得する
function tbox1(){

  var str=document.js.txtb.value;
  /*tagの検出*/
  str = str.replace(/</g, "&amp;lt;");
  str = str.replace(/>/g, "&amp;gt;");
  //alert(str);
  var space = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+"&nbsp;&nbsp;";
  str = space + "&lt;pre&nbsp;class=&quot;box-code&quot;&gt;\n" + str + "&lt;/pre&gt;";
  str = '<pre id="result" class="temp">' + str + "</pre>";
  //ok    "... pre id=\"result\" ..."
  //ok(?) '... pre id=result ...'
  //ng '... pre id=&quot;result&quot; ...'  -> 意味をもたない（エスケープされた）""が生成される
  var form = document.getElementsByName("js")[0];
  form.insertAdjacentHTML('afterend', str);
}


//テキストボックスの文字を操作する
function clr(){
  document.js.txtb.value="";

  //var res = document.getElementById("result");
  var results = document.getElementsByClassName("temp");
  for (var i = results.length-1; i >= 0; i--) {
    results[i].outerHTML = "";
    //alert(index);
  }

  //window.location.reload();
}
