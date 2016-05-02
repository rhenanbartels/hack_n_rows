$( document ).ready(function() {
    $("#convert-form").submit(function(event){
        uploadedFileName = getUploadedFileName();
        selectedExtensionOption = $("#id_options").val();
        uploadedFileExtension = getFileExtension(uploadedFileName);

        if (uploadedFileName == ""){
            showFormErrorLog("Hey, don't forget to select a file");
            event.preventDefault();
        }
        else if (uploadedFileExtension == selectedExtensionOption){
            event.preventDefault();
            showFormErrorLog("Hey, please select a different file extension");
        }

    })

    function showFormErrorLog(msg){
        var customFormError = $("#custom-form-error");
        customFormError.show()
        //Hide pre-existing error logs
        $(".alert alert-danger").hide();
        customFormError.text(msg);
        customFormError.delay(3000).fadeOut();

    }

    function getUploadedFileName(){
        var filename = $('input[type=file]').val().split('\\').pop();
        return filename
    }

    function getFileExtension(filename){
        splittedFileName = filename.split(".");
        return splittedFileName[splittedFileName.length - 1];
    }
});
