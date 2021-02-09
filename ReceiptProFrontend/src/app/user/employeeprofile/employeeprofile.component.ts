import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-employeeprofile',
  templateUrl: './employeeprofile.component.html',
  styleUrls: ['./employeeprofile.component.css']
})
export class EmployeeprofileComponent{
  isEditable:boolean = false;
  userDetails = []
  constructor(private api:ApiService, private router:Router, private activeroute: ActivatedRoute) { }

  presentUserResponse(){
    this.isEditable = true;
  }

  presnetUser = this.api.isSamePresentUser().subscribe(response=> {if(this.activeroute.snapshot.paramMap.get('username') == response){this.presentUserResponse()}},error=>console.log(error))
  getUser = this.api.getEmpDetails(this.activeroute.snapshot.paramMap.get('username'))
            .subscribe(response =>this.userDetails.push(response), error =>console.log(error));
}
