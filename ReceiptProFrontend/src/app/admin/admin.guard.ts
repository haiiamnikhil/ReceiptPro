import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { ApiService } from '../api.service';

@Injectable({
  providedIn: 'root'
})
export class AdminGuard implements CanActivate {
  constructor(private auth:ApiService){}
  
  callBack(response:any){
    console.log(response)
  }

  canActivate(){
    this.auth.isUser().subscribe(user => this.callBack(user))
    return true
  }
}