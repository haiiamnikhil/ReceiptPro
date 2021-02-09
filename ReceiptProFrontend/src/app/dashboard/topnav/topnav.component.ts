import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-topnav',
  templateUrl: './topnav.component.html',
  styleUrls: ['./topnav.component.css']
})
export class TopnavComponent{
  
  name = []
  viewMode = ''
  viewModeState:boolean = false
  constructor(private service:ApiService, private router: Router) { }
  
  getUserName(response:any){
    this.name.push(response)
  }

  toogle(){
    this.viewModeState = !this.viewModeState
  }

  presentUser =  this.service.getPresentUser().subscribe(user => this.getUserName(user))
  

  onSelect(names:any){
    this.router.navigate(['/user/profile',names.username])
  }

  callBack(response:any){
    this.router.navigate(['/login'])
  }

  logoutUser(){
    this.service.logoutUser().subscribe(data =>this.callBack(data),error=>console.log(error))
  }
}