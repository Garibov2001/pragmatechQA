// Page Create
ClassicEditor.create( document.querySelector('#id_content' ), {
    language : 'en',
    toolbar: [ 'heading', '|', 'bold', 'italic', '|', 'link','blockQuote','codeBlock', 
    '|','numberedList','bulletedList','indent','outdent','|','undo','redo'],
    codeBlock: {
        languages: [{ language: 'plaintext', label: 'Plain Code', class: '' }]
}
}).then( id_content => {
    window.id_content = id_content;
}).catch( err => {    
    console.error( err.stack );
} );

