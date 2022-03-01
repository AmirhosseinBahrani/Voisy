const realButton = document.getElementById("inputfile")
const fakeButton = document.getElementById("choose-file")
const directoryText = document.getElementById("choosen-file-directory")

var languageSelectorAudio = document.getElementById("languageSelectorAudio");
var DirAddressAudio = document.getElementById("DirAddressAudio");

var languageSelectorVideo = document.getElementById("languageSelectorVideo");
var DirAddressVideo = document.getElementById("DirAddressVideo");

const TranscribeButtonAudio = document.getElementById("choose-file-audio");
const TranscribeButtonVideo = document.getElementById("choose-file-video");

const FileDirectoryH3ForAudio = document.getElementById("FileDirectoryAudio");
const FileDirectoryH3ForVideo = document.getElementById("FileDirectoryVideo");

const inputfile = document.getElementById('inputfile');
const languageForTranslating = document.getElementById("languageForTranslating");
const textbox = document.getElementById("textbox");

var currentModelDir = "EN";
var requestedTranslateLand = "fa";
var EditorDirFile = "";

fakeButton.addEventListener("click" , function(){
  realButton.click()
  console.log("alo")
});

realButton.addEventListener("change" , function(event){
  if (realButton.value){
    var text = realButton.files[0].name;
    directoryText.innerHTML = text
    console.log(text)
  }else{
    directoryText.innerHTML = "Nothing yet"
  }
});

function readTextFile(file)
{
  var fr=new FileReader();
  fr.readAsText("/Users/amirhosseinsmacbookpro/Documents/Voisy/src/Core/audio/mp3/Dark.srt");
}

function f1() {
    //function to make the text bold using DOM method
    document.getElementById("textarea1").style.fontWeight = "bold";
    var fr=new FileReader();
}

function f2() {
    //function to make the text italic using DOM method
    document.getElementById("textarea1").style.fontStyle = "italic";
}

function f3() {
    //function to make the text alignment left using DOM method
    document.getElementById("textarea1").style.textAlign = "left";
}

function f4() {
    //function to make the text alignment center using DOM method
    document.getElementById("textarea1").style.textAlign = "center";
}

function f5() {
    //function to make the text alignment right using DOM method
    document.getElementById("textarea1").style.textAlign = "right";
}

function f6() {
    //function to make the text in Uppercase using DOM method
    document.getElementById("textarea1").style.textTransform = "uppercase";
}

function f7() {
    //function to make the text in Lowercase using DOM method
    document.getElementById("textarea1").style.textTransform = "lowercase";
}

function f8() {
    //function to make the text capitalize using DOM method
    document.getElementById("textarea1").style.textTransform = "capitalize";
}

function f9() {
    //function to make the text back to normal by removing all the methods applied
    //using DOM method
    document.getElementById("textarea1").style.fontWeight = "normal";
    document.getElementById("textarea1").style.textAlign = "left";
    document.getElementById("textarea1").style.fontStyle = "normal";
    document.getElementById("textarea1").style.textTransform = "capitalize";
    document.getElementById("textarea1").value = " ";
}
function f10() {
  const data = document.getElementById("textarea1").value;
  const textToBLOB = new Blob([data], { type: 'text/plain' });
  const sFileName = 'formData.srt';	   // The file to save the data.
  let newLink = document.createElement("a");
  newLink.download = sFileName;
  if (window.webkitURL != null) {
    newLink.href = window.webkitURL.createObjectURL(textToBLOB);
  }
  else {
    newLink.href = window.URL.createObjectURL(textToBLOB);
    newLink.style.display = "none";
    document.body.appendChild(newLink);
  }
  newLink.click();
}

async function f11(){
  const result = await sendRequestForTranslation()
}

const sendRequestForAudio = async () => {
    try {

      FileDirectoryH3ForAudio.innerHTML = "Loading..."
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
          if (this.readyState == 4) {
              var response = xhttp.responseText;
              if (String(response).charAt(0) == "/"){
                var date = new Date().toLocaleTimeString()


                var UserData = localStorage.getItem("UserData");
                UserDataParsed = JSON.parse(UserData);
                console.log(UserDataParsed);

                if (UserDataParsed == null) {
                  UserDataParsed = [date, response]
                }
                else {
                  UserDataParsed.push(date, response)
                }
                localStorage.setItem("UserData",JSON.stringify(UserDataParsed));
              }
              FileDirectoryH3ForAudio.innerHTML = response

          }
      };
      const text = localStorage.getItem("FileDirectory");
      var newtext = "";
      for (let index = 0; index < text.length; index++) {
          const element = text[index];
          if (element == "/"){
              newtext += "-"
          }
          else {
              newtext += element
          }
      }
      xhttp.open("GET", "http://127.0.0.1:5000/convert/" + newtext + "/" + currentModelDir, true);

      xhttp.onerror = function(error) {
        console.log(error);
        FileDirectoryH3ForAudio.innerHTML = "Error while transcribing, Message:" + error
      }

      xhttp.send();
    } catch (e) {
      console.log("error", e);
      FileDirectoryH3ForAudio.innerHTML = "Error while transcribing, Message:" + e
    }
}

const sendRequestForVideo = async () => {
  try {

    FileDirectoryH3ForVideo.innerHTML = "Loading..."
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            var response = xhttp.responseText;
            FileDirectoryH3ForVideo.innerHTML = response
        }
    };
    const text = localStorage.getItem("FileDirectory");
    var newtext = "";
    for (let index = 0; index < text.length; index++) {
        const element = text[index];
        if (element == "/"){
            newtext += "-"
        }
        else {
            newtext += element
        }
    }
    if (currentModelDir.length >= 5){
      var newdir = "-";
      for (let index = 0; index < currentModelDir.length; index++) {
          const element = currentModelDir[index];
          if (element == "/"){
              newdir += "-"
          }
          else {
              newdir += element
          }
      }
      currentModelDir = newdir
    }
    xhttp.open("GET", "http://127.0.0.1:5000/mp4/" + newtext + "/" + currentModelDir, true);

    xhttp.onerror = function(error) {
      console.log(error);
      FileDirectoryH3ForVideo.innerHTML = "Error while transcribing, Message:" + error
    }

    xhttp.send();
  } catch (e) {
    console.log("error", e);
    FileDirectoryH3ForVideo.innerHTML = "Error while transcribing, Message:" + e
  }
}

const sendRequestForTranslation = async () => {
  try {

    textbox.innerHTML = "Loading..."
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            var response = xhttp.responseText;
            textbox.innerHTML = response
        }
    };
    if (EditorDirFile == ""){
      alert("Please select your srt file")
    }
    else {
      const text = EditorDirFile
      var newtext = "";
      for (let index = 0; index < text.length; index++) {
          const element = text[index];
          if (element == "/"){
              newtext += "-"
          }
          else {
              newtext += element
          }
      }
      xhttp.open("GET", "http://127.0.0.1:5000/translate/" + newtext + "/" + requestedTranslateLand, true);

      xhttp.onerror = function(error) {
        console.log(error);
        textbox.innerHTML = "Error while translating, Message:" + error
      }
      xhttp.send();
    }


  } catch (e) {
    console.log("error", e);
    textbox.innerHTML = "Error while translating, Message:" + e
  }
}

inputfile.addEventListener('change', function(event) {

    var fr=new FileReader();
    fr.onload=function(){
        document.getElementById('textarea1')
                .textContent=fr.result;
    }
    fr.readAsText(this.files[0]);

    EditorDirFile = (event.target.files)[0].path;
})

languageForTranslating.addEventListener("change", function(event) {
  requestedTranslateLand = event.target.value
  console.log(requestedTranslateLand)
})
TranscribeButtonAudio.addEventListener("click", async (event) => {
    FileDirectoryH3ForAudio.innerHTML = "Sending"
    const res = await sendRequestForAudio()
})

TranscribeButtonVideo.addEventListener("click", async (event) => {
    FileDirectoryH3ForVideo.innerHTML = "Sending"
    const res = await sendRequestForVideo()
})

languageSelectorAudio.addEventListener("change", (e) => {
  if (String(e.target.value) == "etc"){
    DirAddressAudio.style.display = "block"
  }
  else {
    DirAddressAudio.style.display = "none"
    currentModelDir = String(e.target.value)
  }
})

DirAddressAudio.addEventListener("input", (e) => {
  currentModelDir = String(e.target.value)
})

languageSelectorVideo.addEventListener("change", (e) => {
  if (String(e.target.value) == "etc"){
    DirAddressVideo.style.display = "block"
  }
  else {
    DirAddressVideo.style.display = "none"
    currentModelDir = String(e.target.value)
  }
})

DirAddressVideo.addEventListener("input", (e) => {
  currentModelDir = String(e.target.value)
})
