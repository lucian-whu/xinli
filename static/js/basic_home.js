$(function() {
  $(".typed").typed({
    strings: [
      "stat lucian.human<br/>" +
      "><span class='caret'>$</span> focus: text mining, informetrics, medical informatics, NLP.<br/> ^100" +
      "><span class='caret'>$</span> programming: Python, java, R<br/> ^300" +
      "><span class='caret'>$</span> alias: lucian, 爱吃花生的小松鼠 <br/>" +
      "><span class='caret'>$</span> tool: numpy, pandas, matplotlib, mxnet, lucene, NLTK.<br/>" +
      "><span class='caret'>$</span> organization: PhD.student @<a href='http://www.whu.edu.cn/'>Wuhan University</a><br/> ^100" +
      "><span class='caret'>$</span> <a href='/timeline'>timeline</a> <a href='https://github.com/lucian-whu'>github</a> <a href='https://www.linkedin.com/in/xin-li-89a82111a/''>linkedin</a><br/>"
    ],
    showCursor: true,
    cursorChar: '_',
    autoInsertCss: true,
    typeSpeed: 1,
    startDelay: 200,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});