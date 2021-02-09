import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent{


  details= []
  constructor(private userDetails:ApiService, private router:Router) { }

  callBack(response:any) {
    this.details.push(response)
  }

  status = this.userDetails.getUserDetails().subscribe(response=> this.callBack(response),error=>console.log(error))
}
