import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {
  doc:File
  filename:string
  doc_type:string = "RSD"
  constructor(private api:ApiService, private router:Router) { }

  ngOnInit(): void {
  }

  onFileAdded(event:any){
    if (event.target.files.length > 0){
      this.doc = event.target.files[0]
      console.log(this.doc)
    }
  }

  upload(){
    const data = new FormData()
    data.append('file', this.doc,this.doc.name)
    data.append('doc_type',this.doc_type)
    this.api.uploadData(data).subscribe(response =>console.log(response),error =>console.log(error))
  }
}
