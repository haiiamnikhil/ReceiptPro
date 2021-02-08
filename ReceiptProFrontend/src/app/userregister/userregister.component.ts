import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserregisterService } from './userregister.service';

@Component({
  selector: 'app-userregister',
  templateUrl: './userregister.component.html',
  styleUrls: ['./userregister.component.css']
})

export class UserregisterComponent{

  constructor(private service:UserregisterService, private router:Router) {}

  username: string
  password:string
  email:string;
  first_name:string
  last_name:string
  gender:string
  emp_id:string
  employ_department:string
  employ_designation:string
  date_joined:string
  shift_id:string
  team_lead_id:string
  team_lead_name:string
  team_lead_mail:string
  company_worker_id:string
  employ_role:string
  appointment_status:string
  user_name:any
  errors:any
  image:File
  users = []
  generateUsername(){
    this.user_name = this.email.split("@",1)
    this.username = this.user_name.toString()
  }

  listUsers(){
    this.service.listUsers().subscribe(data =>this.users=data)
  }

  callbacks(response:any){
    let status = response['status']
    if (status == true){
      this.router.navigate(['/login'])
    }
    else{
      this.errors = status['Errors']
      this.router.navigate(['/register'])
    }
  }

  getFile(event:any){
    if (event.target.files.length > 0){
      const file = event.target.files[0]
      this.image = file
      console.log(this.image)
    }
  }

  registerUser(){
    let details = {
      username:this.username,
      password:this.password,
      email:this.email,
      first_name:this.first_name,
      last_name:this.last_name,
      gender:this.gender,
      profile_image:this.image
    }
    console.log(details.profile_image)
    this.service.register(details).subscribe(data => this.callbacks(data),error => console.log(error));
  }
}