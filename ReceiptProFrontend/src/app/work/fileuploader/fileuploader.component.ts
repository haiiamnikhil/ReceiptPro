import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-fileuploader',
  templateUrl: './fileuploader.component.html',
  styleUrls: ['./fileuploader.component.css']
})
export class FileuploaderComponent implements OnInit {

  viewMode = ''

  constructor(private api:ApiService, private router:Router) { }

  ngOnInit(): void {
    console.log(this.viewMode)
  }

}
