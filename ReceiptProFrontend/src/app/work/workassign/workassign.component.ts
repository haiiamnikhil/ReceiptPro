import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-workassign',
  templateUrl: './workassign.component.html',
  styleUrls: ['./workassign.component.css']
})
export class WorkassignComponent implements OnInit {
  number: number = 0
  presentvalue:number
  constructor() { }

  ngOnInit(): void {

  }

  onIncrement(){
    this.number = this.presentvalue + 1
  }

  onDecrement(){
    this.number -this.presentvalue - 1
  }
}
