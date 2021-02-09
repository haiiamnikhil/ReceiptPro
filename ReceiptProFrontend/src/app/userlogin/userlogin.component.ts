import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-userlogin',
  templateUrl: './userlogin.component.html',
  styleUrls: ['./userlogin.component.css']
})
export class UserloginComponent{
  username:string
  password:string
  login_status:boolean
  err:string
 
  public currentUser:string
  constructor(private login: ApiService, private router:Router) { }

  callbacks(response:any){
    this.login_status = response['login_status']
    this.err = status['message']
    if(this.login_status == true){
      this.router.navigate(['/user/dashboard'])
    }
    else{
      this.username = ''
      this.password = ''
    }
  }

  onClickLogin(){
    let details = {
      username:this.username,
      password:this.password
    }
    this.login.loginUser(details).subscribe(response =>this.callbacks(response));
  }
}
