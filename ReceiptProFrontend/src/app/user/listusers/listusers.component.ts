import { Component, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-listusers',
  templateUrl: './listusers.component.html',
  styleUrls: ['./listusers.component.css']
})
export class ListusersComponent{
  @Output() username:string 
  public page = 1
  public pageSize = 10
  users = []
  isEditable:boolean = false
  constructor(private api:ApiService, private router: Router) { }

  callBack(response:any){ 
    this.users.push(response)
    console.log(this.users)
  }

  getusers = this.api.getAllUsers().subscribe(response => this.callBack(response),error =>console.log(error))

  presentUserResponse(){
    this.isEditable = true
  }

  onSelect(person:any){
    this.router.navigate(['/emp-profile',person.username])
  }
} 