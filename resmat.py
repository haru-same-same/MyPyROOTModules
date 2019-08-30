#-------------------------------------------------
#import
#-------------------------------------------------

import numpy as np
import ROOT as rt

#-------------------------------------------------
#Class
#-------------------------------------------------

class Resmat:
    #Set Original File Path and Tree Name
    def SetFileTreeBranch(self, File, Tree, xBranch, yBranch):
        self.File = File
        self.Tree = Tree
        self.xBranch = xBranch
        self.yBranch = yBranch
    
    #Set Bin Edge
    def SetBinEdge(self, EdgeList):
        self.BinEdge = np.array(EdgeList, dtype = 'float64')
        self.NBins = len(EdgeList) - 1
    
    #Set Number of Events
    def SetNEvents(self, NEvents):
        self.NEvents = NEvents
    
    #Create Response Matrix
    def CreateResMat(self):
        #Load ROOT File
        tf = rt.TFile(self.File)
        
        #Load TTree
        tr = tf.Get(self.Tree)
        
        #Declare Histograms
        raw_histo = rt.TH2D('raw_histo', 'raw_histo', self.NBins, self.BinEdge, self.NBins, self.BinEdge)
        resmat_histo = rt.TH2D('resmat_histo', 'resmat_histo', self.NBins, 0, self.NBins + 1, self.NBins, 0, self.NBins + 1)
        
        #Event Loop
        for j in xrange(self.NEvents):
            tr.GetEntry(j)
            Branchx = getattr(tr, self.xBranch)
            Branchy = getattr(tr, self.yBranch)
            raw_histo.Fill(Branchx, Branchy)
        
        #Resmat Fill Loop
        for x in range(1,self.NBins + 1):
            if raw_histo.Integral(x, x, 1, self.NBins) > 0:
                for y in range(1, self.NBins + 1):
                    BinNum = raw_histo.GetBin(x, y)
                    resmat_histo.SetBinContent(BinNum, raw_histo.Integral(x, x, y, y)/raw_histo.Integral(x, x, 1, self.NBins))
        
        #Draw
        c1 = rt.TCanvas('c1', 'c1', 700, 700)
        rt.gStyle.SetPaintTextFormat('0.3f')
        rt.gPad.SetLeftMargin(0.16)
        rt.gPad.SetRightMargin(0.11)
        resmat_histo.SetMarkerSize(1.5)
        resmat_histo.GetZaxis().SetRangeUser(0., 1.)
        resmat_histo.SetTitle('Response Matrix')
        resmat_histo.SetXTitle(self.xBranch + '[GeV/c^{2}]')
        resmat_histo.SetYTitle(self.yBranch + '[GeV/c^{2}]')
        for j in range(1,self.NBins + 1):
            resmat_histo.GetXaxis().SetBinLabel(j, str(int(self.BinEdge[j - 1])) + '-' + str(int(self.BinEdge[j])))
            resmat_histo.GetYaxis().SetBinLabel(j, str(int(self.BinEdge[j - 1])) + '-' + str(int(self.BinEdge[j])))
        resmat_histo.GetXaxis().SetNdivisions(self.NBins + 1, 0, 0, rt.kFALSE)
        resmat_histo.GetYaxis().SetNdivisions(self.NBins + 1, 0, 0, rt.kFALSE)
        resmat_histo.Draw('text, colz')
        resmat_histo.SetStats(0)
        c1.SaveAs('resmat.pdf')

