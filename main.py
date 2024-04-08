import planesections as ps
import matplotlib.pyplot as plt
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/beam')
async def root(request: Request):
    data = await request.json()
    
    p1 = data.get('p1')
    p2 = data.get('p2')
    x2 = data.get('x2')
    x1 = data.get('x1')
    vS = data.get('vS')
    vE = data.get('vE')
    vL1 = data.get('vL1')
    vL2 = data.get('vL2')
    
    beamLength = data.get('beamLength')
    supportA = data.get('supportA')
    supportB = data.get('supportB')
    
    try:
        L = float(beamLength)
        l1 = float(x1)
        p1 = float(p1)
        l2 = float(x2)
        p2 = float(p2)
        w1 = float(vS)
        w2 = float(vE)
        x1 = float(vL1)
        x2 = float(vL2)
        A = float(supportA)
        B = float(supportB)

        beam = ps.newEulerBeam(L)
        
        pinned = [1, 1, 0]  # Support condition
        beam.setFixity(A, pinned)
        beam.setFixity(B, pinned)

        beam.addLabel(A, label='A')
        beam.addLabel(x1, label='E')
        beam.addLabel(x2, label='F')
        beam.addLabel(B, label='B')
        beam.addVerticalLoad(p1, l1, label='C')
        beam.addVerticalLoad(p2, l2, label='D')


        newList = [[0,0], [w1, w2]]

        beam.addLinLoad(x1, x2, newList)  
        

        analysis = ps.PyNiteAnalyzer2D(beam)


        analysis.runAnalysis()

        # Plot and show the diagrams
        fig_beam = plt.figure()
        ps.plotBeamDiagram(beam)
        plt.title("Beam Diagram")
        plt.show()

        # Output a success message
        return {'msg': ("Success", "Analysis completed successfully!")}
        
    except:
        print("")
      


@app.post('/shear')
async def shear(request: Request):
    data = await request.json()
    
    p1 = data.get('p1')
    p2 = data.get('p2')
    x2 = data.get('x2')
    x1 = data.get('x1')
    vS = data.get('vS')
    vE = data.get('vE')
    vL1 = data.get('vL1')
    vL2 = data.get('vL2')
    
    beamLength = data.get('beamLength')
    supportA = data.get('supportA')
    supportB = data.get('supportB')
    
    try:
        L = float(beamLength)
        l1 = int(x1)
        p1 = int(p1)
        l2 = int(x2)
        p2 = int(p2)
        w1 = float(vS)
        w2 = float(vE)
        x1 = float(vL1)
        x2 = float(vL2)
        A = float(supportA)
        B = float(supportB)

        print(L, l1, l2, p1, p2, w1, w2, x1, x2, A, B)
        beam = ps.newEulerBeam(L)
        
        pinned = [1, 1, 0]  # Support condition
        beam.setFixity(A, pinned)
        beam.setFixity(B, pinned)

        beam.addLabel(A, label='A')
        beam.addLabel(x1, label='E')
        beam.addLabel(x2, label='F')
        beam.addLabel(B, label='B')
        beam.addVerticalLoad(p1, l1, label='C')
        beam.addVerticalLoad(p2, l2, label='D')
        print(x1, x2, [w1, w2])
        print(type(beam))

        newList = [[w1,w2], [0, 0]]

        beam.addLinLoad(x1, x2, newList)
        

        analysis = ps.PyNiteAnalyzer2D(beam)


        analysis.runAnalysis()

        # Plot and show the diagrams
        # fig_shear = plt.figure()
        ps.plotShear(beam, scale=1, yunit='kN')
        plt.title("Shear Force Diagram")
        plt.show()

        # Output a success message
        return {'msg': ("Success", "Analysis completed successfully!")}
        
    except ValueError:
        return {'msg': ("Error", "Please enter valid numerical values.")} 


@app.post('/moment')
async def moment(request: Request):
    data = await request.json()
    
    p1 = data.get('p1')
    p2 = data.get('p2')
    x2 = data.get('x2')
    x1 = data.get('x1')
    vS = data.get('vS')
    vE = data.get('vE')
    vL1 = data.get('vL1')
    vL2 = data.get('vL2')
    
    beamLength = data.get('beamLength')
    supportA = data.get('supportA')
    supportB = data.get('supportB')
    
    try:
        L = float(beamLength)
        l1 = int(x1)
        p1 = int(p1)
        l2 = int(x2)
        p2 = int(p2)
        w1 = float(vS)
        w2 = float(vE)
        x1 = float(vL1)
        x2 = float(vL2)
        A = float(supportA)
        B = float(supportB)

        beam = ps.newEulerBeam(L)
        
        pinned = [1, 1, 0]  # Support condition
        beam.setFixity(A, pinned)
        beam.setFixity(B, pinned)

        beam.addLabel(A, label='A')
        beam.addLabel(x1, label='E')
        beam.addLabel(x2, label='F')
        beam.addLabel(B, label='B')
        beam.addVerticalLoad(p1, l1, label='C')
        beam.addVerticalLoad(p2, l2, label='D')
        # print(x1, x2, [w1, w2])
        # print(type(beam))

        newList = [[w1,w2], [0, 0]]

        beam.addLinLoad(x1, x2, newList)
        

        analysis = ps.PyNiteAnalyzer2D(beam)


        analysis.runAnalysis()

        # Plot and show the diagrams
        # fig_shear = plt.figure()


        # fig_moment = plt.figure()
        ps.plotMoment(beam, scale=1, yunit='kNm')
        plt.title("Bending Moment Diagram")
        plt.show()


        # Output a success message
        return {'msg': ("Success", "Analysis completed successfully!")}
        
    except ValueError:
        return {'msg': ("Error", "Please enter valid numerical values.")} 
      
